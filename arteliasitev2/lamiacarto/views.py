from django.shortcuts import render, redirect
import json
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

# Create your views here.

# * ******************************************************************************
# * ************************** API ***********************************


class APIFactory:

    renderer_classes = [JSONRenderer]

    def getresult(**kwargs):
        print("APIFactory", kwargs)
        projectid = kwargs.get("project_id")

        lamiaparser = LamiaSession.getInstance(projectid).lamiaparser

        tablename = kwargs.get("tablename", None)

        if tablename is None:
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
        jsonresult = APIFactory.getresult(**kwargs)
        # yourdata = [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        # results = PostSerializer(yourdata, many=True).data
        return Response(jsonresult)
        # return JsonResponse(jsonresult)

    def post(self, request, **kwargs):
        print("***", kwargs)
        print(request.POST)
        # print(request.headers)
        print(request.data)
        yourdata = [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = PostSerializer(yourdata, many=True).data
        return Response(results)


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
            lamiassession = LamiaSession.getInstance(projectid)
            nearestpk, dist = lamiassession.getNearestPk(
                request.data["layer"], request.data["coords"]
            )

            geom = lamiassession.qgscanvas.getQgsGeomFromPk(
                lamiassession.lamiaparser, request.data["layer"], nearestpk
            )
            geomson = geom.asJson()
            result = json.dumps({"nearestpk": nearestpk, "dist": dist, "geom": geomson})
            # logging.getLogger().debug(f"nearest {result}")
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

        context = json.dumps(list(queryset.values("id_project", "qgisserverurl"))[0])

        request.session["idproject"] = idproject
        if idproject > 1 and not request.user.is_authenticated:
            return redirect("home")

        return render(request, self.mytemplate, {"context": context})

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)
