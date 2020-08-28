from django.shortcuts import render, redirect
import json, os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import arteliasitev2.qwc2.scripts.themesConfig as themesConfig

from rest_framework import views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from .serializers import PostSerializer

from .models import User, Project
from .lamiaforsession import LamiaSession
import logging
import qgis.core

import threading


# Create your views here.

# * ******************************************************************************
# * ************************** API ***********************************


class APIFactory_:

    renderer_classes = [JSONRenderer]

    def getresult(request, **kwargs):
        print("APIFactory", kwargs)

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


class PostViewSet(views.APIView):
    def get(self, request, **kwargs):
        print("kwargs", kwargs)
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


class LamiaFuncAPI(views.APIView):
    def get(self, request, **kwargs):
        projectid = kwargs.get("project_id")
        lamiassession = LamiaSession.getInstance(projectid)
        return Response(None)

    def post(self, request, **kwargs):

        """ 
        in kwargs : get url arguments : ex kwargs.get("project_id")
        in request.POST : get values sent b html formular
            ex         id = request.POST.get("id")  (where id is id of html form)
                        pw = request.POST.get("pw")
        IN request.data : get data sent with post from client
        in   request.session : you can set or get values
            ex :   request.session["idproject"] = idproject
            print(request.session.items())
        """
        projectid = kwargs.get("project_id")

        if request.data["func"] == "nearest":
            print("launch", request.data)
            # lamiasession=LamiaSession.getInstance(projectid)
            # t = threading.Thread(
            #     name="Qgis", target=LamiaSession.getInstance(projectid)
            # )
            # t.start()
            # res = t.join()
            # print('')
            # lamiassession = LamiaSession.getInstance(projectid)
            print(threading.current_thread().name)
            nearestpk = LamiaSession.getInstance(projectid).getNearestPk(
                request.data["layer"], request.data["coords"]
            )
            # t = threading.Thread(
            #     name="Qgis",
            #     target=LamiaSession.getInstance(projectid).getNearestPk(
            #         request.data["layer"], request.data["coords"]
            #     ),
            # )
            # t.start()
            # res = t.join()
            # print("ok id", res)
            # print(threading.current_thread().name)

            # geom = lamiassession.qgscanvas.getQgsGeomFromPk(
            #     lamiassession.lamiaparser, request.data["layer"], nearestpk
            # )
            # geomson = geom.asJson()
            geomson = None

            # result = json.dumps({"nearestpk": nearestpk, "dist": dist, "geom": geomson})
            result = json.dumps({"nearestpk": nearestpk})
            # logging.getLogger().debug(f"nearest {result}")
            print("sendres")
            return Response(result)

        return Response(None)


# * ******************************************************************************
# * ************************** Views ***********************************


class BaseView(View):
    mytemplate = "base.html"

    def get(self, request):
        logging.getLogger().debug("BaseView")

        if request.user.is_authenticated:
            return self.loggedUser(request)
        else:
            return self.notloggedUser(request)

    def post(self, request, **kwargs):

        id = request.POST.get("id")
        pw = request.POST.get("pw")
        user = authenticate(username=id, password=pw)

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            login(request, user)
            return self.loggedUser(request)

        else:
            logout(request)
            return redirect("home")

    def loggedUser(self, request):
        queryset = Project.objects.filter(users__username=request.user)
        return render(request, self.mytemplate, {"projects": queryset})

    def notloggedUser(self, request):
        request.session["idproject"] = 1
        context = {"mytext": "popo"}
        queryset = Project.objects.filter(id_project=1)
        return render(
            request,
            BaseView.mytemplate,
            {"context": json.dumps(context), "projects": queryset},
        )


class LamiaProjectView(BaseView):
    mytemplate = "lamiacarto/index.html"

    def get(self, request, **kwargs):
        logging.getLogger().debug("LamiaProjectView")

        print("kwargs", kwargs)

        queryset = Project.objects.filter(id_project=kwargs.get("project_id"))
        idproject = queryset.values("id_project")[0]["id_project"]

        # LamiaSession.getInstance(idproject)

        context = json.dumps(
            list(
                queryset.values("id_project", "qgisserverurl", "pgdbname", "pgschema")
            )[0]
        )

        request.session["idproject"] = idproject
        if idproject > 1 and not request.user.is_authenticated:
            return redirect("home")

        conffile = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "qwc2config",
            "themesConfig_lamia.json",
        )

        datab = json.dumps(themesConfig.genThemes(conffile))
        return render(request, self.mytemplate, {"context": context, "themes": datab})

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)
