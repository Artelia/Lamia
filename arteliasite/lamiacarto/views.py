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

# Create your views here.


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


class BaseView(View):
    mytemplate = "base.html"

    def get(self, request):
        # print("***", request.session.keys())
        print("SESSION : ", request.session)
        print("SESSION items : ", request.session.items(), request.session.session_key)
        # print("***", request.session.session_key)
        if request.user.is_authenticated:
            return self.loggedUser(request)
        else:
            return self.notloggedUser(request)

    def post(self, request, **kwargs):
        # print("post", request.POST)
        # print(request.POST.dict())
        # print(request.POST.items())

        # if 'login' in request.POST.items()

        id = request.POST.get("id")
        pw = request.POST.get("pw")
        user = authenticate(username=id, password=pw)

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            login(request, user)
            # Redirect to a success page.
            # return HttpResponseRedirect("/account/loggedin/")
            return self.loggedUser(request)

        else:
            logout(request)
            # return self.notloggedUser(request)
            return redirect("home")

    def loggedUser(self, request):

        queryset = Project.objects.filter(users__username=request.user)
        return render(request, self.mytemplate, {"projects": queryset})

    def notloggedUser(self, request):
        # return redirect("home")
        print(request)
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
        # context = {"mytext": "popo"}
        # print('ùù')
        # print(request.GET)
        # print(kwargs)
        print("***", request.session.items())

        queryset = Project.objects.filter(id_project=kwargs.get("project_id"))
        idproject = queryset.values("id_project")[0]["id_project"]

        LamiaSession.getInstance(idproject)
        # queryset = Project.objects.filter(id_project=idproject)
        # queryval = queryset.values()[0]
        # print(queryval["qgisserverurl"])
        # lamiaparser.loadDBase(
        #     dbtype="Postgis",
        #     host=queryval["pghost"],
        #     # host="localhost",
        #     port=queryval["pgport"],
        #     dbname=queryval["pgdbname"],
        #     schema=queryval["pgschema"],
        #     user=queryval["pguser"],
        #     password=queryval["pgpassword"],
        # )

        # print("**", queryset.values("id_projet", "qgisserverurl"))
        context = json.dumps(list(queryset.values("id_project", "qgisserverurl"))[0])
        print("SESSION : ", request.session)
        request.session["idproject"] = idproject
        if idproject > 1 and not request.user.is_authenticated:
            return redirect("home")

        # print(queryset.values)
        # context = queryset[0].as_dict()
        # # dictionaries = [ obj.as_dict() for obj in self.get_queryset() ]
        # print(list(queryset))
        # print(context)

        # return render(request, self.mytemplate, {"context": json.dumps(context)})

        return render(request, self.mytemplate, {"context": context})

    def post(self, request, **kwargs):
        return BaseView.post(self, request, **kwargs)
