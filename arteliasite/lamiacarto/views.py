from django.shortcuts import render, redirect
import json, os, sys, base64
from django.conf import settings

sys.path.append(settings.BASE_DIR)
import qwc2.scripts.themesConfig as themesConfig

from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

from artelialogin.models import User, Project
from artelialogin.views import BaseView
import logging, pprint
from urllib.parse import urlparse, urlunsplit, urlsplit

# Create your views here.


def userCanAccessProject(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        id_project = kwargs.get("project_id", None)
        if (
            isinstance(id_project, int)
            and id_project > 1
            and not request.user.is_authenticated
        ):
            return redirect("home")
        return view_func(request, *args, **kwargs)

    return _wrapped_view_func


# * ******************************************************************************
# * ************************** API ***********************************


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaCartoAPIView(views.APIView):
    def get(self, request, **kwargs):
        projectid = kwargs.get("project_id")
        tablename = kwargs.get("tablename", None)

        if tablename == "config.json":
            configpath = fn = os.path.join(
                os.path.dirname(__file__), "qwc2config", "config.json"
            )
            with open(configpath) as f:
                data = json.load(f)
            return Response(data)

        elif tablename == "themes.json":
            if settings.PROXY_ARTELIA:
                conffile = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "qwc2config",
                    "themesConfig_lamia_proxy.json",
                )
            else:
                os.environ["HTTP_PROXY"] = ""
                os.environ["HTTPS_PROXY"] = ""
                conffile = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "qwc2config",
                    "themesConfig_lamia.json",
                )

            with open(conffile) as f:
                themesdata = json.load(f)

            # print('***PROXY***', os.environ["HTTP_PROXY"], os.environ["HTTPS_PROXY"])

            queryset = Project.objects.filter(id_project=projectid)
            qgisserverurl = queryset.values("qgisserverurl")[0]["qgisserverurl"]
            themesdata["themes"]["items"][0]["url"] = qgisserverurl
            themesConfig.qwc2_path = "./lamiacarto/static"

            # print('gentehems')
            datab = themesConfig.genThemes(themesdata)
            # print(datab)
            datab = self.replaceURLinGenThemes(datab,qgisserverurl,projectid)
            # print('response',datab)
            return Response(datab)

        elif tablename.split("/")[0] == "translations":
            translationfile = os.path.join(settings.BASE_DIR, tablename)
            with open(translationfile, encoding="utf8") as f:
                data = json.load(f)
            return Response(data)

    def post(self, request, **kwargs):
        pass



    def replaceURLinGenThemes(self,genthemes,qgisserverurl,projectid):
        websiteurl = os.getenv('LAMIA_URL',"http://localhost:8000/qgisserver")
        websiteurl += '/' + str(projectid)
        parsed_qgisserverurl = urlparse(qgisserverurl)
        parsed_qgisserverurl = parsed_qgisserverurl._replace(query="")
        qgisserverurl = parsed_qgisserverurl.geturl()

        if isinstance(genthemes, dict):
            for k, v in genthemes.items():
                genthemes[k] = self.replaceURLinGenThemes(v,qgisserverurl,projectid)
        elif isinstance(genthemes, list):
            for i, e in enumerate(genthemes) :
                genthemes[i] = self.replaceURLinGenThemes(e,qgisserverurl,projectid)
        elif isinstance(genthemes, str):
            if qgisserverurl in genthemes:
                genthemes = genthemes.replace(qgisserverurl, websiteurl)
        return genthemes

# * ******************************************************************************
# * ************************** View ***********************************


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaProjectView(BaseView):
    mytemplate = "lamiacarto/index.html"

    def get(self, request, **kwargs):
        # print("*", kwargs)
        id_project = kwargs.get("project_id", None)

        url1 = kwargs.get("conffile", None)
        if url1:
            redirection = self.redirect(url1, request)
            if redirection:
                return redirection

        if id_project is None:
            return redirect("lamiaprojectgis", project_id=request.session["idproject"])

        request.session["idproject"] = id_project
        queryset = Project.objects.filter(id_project=id_project)
        context = json.dumps(
            list(
                queryset.values("id_project", "qgisserverurl", "pgdbname", "pgschema")
            )[0]
        )

        queryset = Project.objects.filter(users__username=request.user)

        return render(
            request, self.mytemplate, {"context": context, "projects": queryset},
        )

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)

    def redirect(self, url1, request):
        if url1 == "config.json":
            return redirect(
                "lamiacartoapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1 == "themes.json":
            return redirect(
                "lamiacartoapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1.split("/")[0] == "translations":
            return redirect(
                "lamiacartoapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1.split("/")[0] == "assets":
            return redirect("/static/" + url1)

        else:
            # print("*", url1)
            return redirect("lamiaprojectgis")

