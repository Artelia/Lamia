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
            result = json.dumps(list(queryset.values())[0])
            return result

        if tablename == "dbasetables":
            dbasetables = lamiaparser.dbasetables
            return dbasetables

        elif tablename == "styles":
            stylesconf = LamiaSession.getInstance(projectid).getStyles()
            return stylesconf


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaApiView(views.APIView):
    def get(self, request, **kwargs):
        # print("kwargs", kwargs)
        jsonresult = APIFactory.getresult(request, **kwargs)
        return Response(jsonresult)

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

            elif func == "thumbnail":
                pkres = request.data["pkresource"]
                bindata = LamiaSession.getInstance(projectid).getThumbnail(pkres)
                bindata = base64.b64encode(bindata)
                return Response({"base64thumbnail": bindata})

        else:
            if func == "dbasetables":
                locale = request.data["locale"]
                lamiasession.updateLocale(locale)
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

            elif func == "bboxfilter":
                # table = request.data["tablename"]
                bbox = request.data["bbox"]
                res = LamiaSession.getInstance(projectid).getPksFromBBox(
                    tablename, bbox
                )
                print("**", res)
                return Response(res)

