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
import logging


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


# * ******************************************************************************
# * ************************** View ***********************************


@method_decorator(userCanAccessProject, name="dispatch")
class LamiaReportView(BaseView):
    mytemplate = "lamiareport/index.html"

    def get(self, request, **kwargs):
        print("*", kwargs)
        id_project = kwargs.get("project_id", None)
        if id_project is None:
            # print(request.session["idproject"])
            return redirect(
                "lamiaprojectreport", project_id=request.session["idproject"]
            )

        return render(request, self.mytemplate)

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)

