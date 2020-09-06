from django.shortcuts import render, redirect
import json, os, sys
from django.conf import settings

sys.path.append(settings.BASE_DIR)
import qwc2.scripts.themesConfig as themesConfig

from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator

# from .serializers import PostSerializer

from artelialogin.models import User, Project
from artelialogin.views import BaseView
from .lamiaforsession import LamiaSession
import logging
import qgis.core

import threading
from functools import wraps


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


class APIFactory:

    renderer_classes = [JSONRenderer]

    def getresult(request, **kwargs):
        # print("APIFactory", kwargs)

        projectid = kwargs.get("project_id")
        tablename = kwargs.get("tablename", None)
        lamiaparser = LamiaSession.getInstance(projectid).lamiaparser

        if tablename is None:  # request on project
            queryset = Project.objects.filter(id_project=projectid)
            # id_projet = queryset.values("id_projet")[0]
            # print(queryset.values_list())
            # print(queryset.values())
            result = json.dumps(list(queryset.values())[0])
            # json.dumps(list(queryset.values("id_projet", "qgisserverurl"))[0])
            # print(type(result), result)
            return result

        if tablename == "dbasetables":
            dbasetables = lamiaparser.dbasetables
            return dbasetables

        elif tablename == "themes.json":
            conffile = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "qwc2config",
                "themesConfig_lamia.json",
            )
            with open(conffile) as f:
                themesdata = json.load(f)

            queryset = Project.objects.filter(id_project=projectid)
            qgisserverurl = queryset.values("qgisserverurl")[0]["qgisserverurl"]
            themesdata["themes"]["items"][0]["url"] = qgisserverurl

            datab = themesConfig.genThemes(themesdata)

            return datab

        elif tablename.split("/")[0] == "translations":
            translationfile = os.path.join(settings.BASE_DIR, tablename)
            print(translationfile)
            with open(translationfile, encoding="utf8") as f:
                data = json.load(f)
            return data

        elif tablename == "config.json":
            configpath = fn = os.path.join(
                os.path.dirname(__file__), "qwc2config", "config.json"
            )
            with open(configpath) as f:
                data = json.load(f)
            return data


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaApiView(views.APIView):
    def get(self, request, **kwargs):
        # print("kwargs", kwargs)
        jsonresult = APIFactory.getresult(request, **kwargs)
        # yourdata = [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        # results = PostSerializer(yourdata, many=True).data
        return Response(jsonresult)
        # return JsonResponse(jsonresult)

    def post(self, request, **kwargs):
        projectid = kwargs.get("project_id")
        tablename = kwargs.get("tablename", None)
        lamiasession = LamiaSession.getInstance(projectid)
        lamiaparser = lamiasession.lamiaparser
        # threading.current_thread().name
        # if threading.current_thread().name in lamiasession.cursors.keys()
        # lamiaparser.PGiscursor = None  # force thread safe cursor
        func = request.data["function"]

        if tablename is None:  # request on project
            if func == "dbasetables":
                dbasetables = lamiaparser.dbasetables
                return Response(dbasetables)

        else:

            if func == "dbasetables":
                qgistables = [tablename] + lamiaparser.getParentTable(tablename)
                dbtableresponse = {}
                for table in qgistables:
                    # res = {**dict1, **dict2}
                    dbtableresponse = {
                        **dbtableresponse,
                        **lamiaparser.dbasetables[table]["fields"],
                    }
                # dbasetables = lamiaparser.dbasetables[tablename]
                return Response(dbtableresponse)

            elif func == "nearest":
                nearestpk = LamiaSession.getInstance(projectid).getNearestPk(
                    tablename, request.data["coords"]
                )
                result = json.dumps({"nearestpk": nearestpk})
                return Response(result)

            elif func == "getids":
                confobject = type("confobject", (object,), {})
                confobject.DBASETABLENAME = tablename
                confobject.PARENTJOIN = request.data["parentjoin"]
                if "tablefilterfield" in request.data.keys():
                    confobject.TABLEFILTERFIELD = request.data["tablefilterfield"]
                if "choosertreewdgspec" in request.data.keys():
                    confobject.CHOOSERTREEWDGSPEC = request.data["choosertreewdgspec"]

                confobject.parentWidget = type("confobject", (object,), {})
                confobject.parentWidget.DBASETABLENAME = request.data["parenttablename"]
                confobject.parentWidget.currentFeaturePK = request.data["parentpk"]

                ids = LamiaSession.getInstance(projectid).getIds(confobject)
                return Response(ids)


# * ******************************************************************************
# * ************************** Views ***********************************


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaProjectView(BaseView):
    mytemplate = "lamiacarto/index.html"

    def get(self, request, **kwargs):
        print("*", kwargs)
        id_project = kwargs.get("project_id")

        url1 = kwargs.get("conffile", None)
        if url1:
            redirection = self.redirect(url1, request)
            if redirection:
                return redirection

        request.session["idproject"] = id_project
        queryset = Project.objects.filter(id_project=id_project)
        context = json.dumps(
            list(
                queryset.values("id_project", "qgisserverurl", "pgdbname", "pgschema")
            )[0]
        )

        queryset = Project.objects.filter(users__username=request.user)

        return render(
            request, self.mytemplate, {"context": context, "projects": queryset}
        )

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)

    def redirect(self, url1, request):
        if url1 == "config.json":
            return redirect(
                "lamiaapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1 == "themes.json":
            return redirect(
                "lamiaapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1.split("/")[0] == "translations":
            return redirect(
                "lamiaapi", project_id=request.session["idproject"], tablename=url1
            )
        elif url1.split("/")[0] == "assets":
            return redirect("/static/" + url1)

        else:
            print("*", url1)
            return redirect("lamiaproject")

