from django.shortcuts import render, redirect
import json
from rest_framework import views
from rest_framework.response import Response
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from .serializers import PostSerializer

from .models import User, Project

# Create your views here.


def index(request):
    context = {"mytext": "popo"}
    return render(request, "lamiacarto/index.html", {"context": json.dumps(context)})


class PostViewSet(views.APIView):
    def get(self, request):
        yourdata = [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = PostSerializer(yourdata, many=True).data
        return Response(results)

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
        print(request)
        context = {"mytext": "popo"}
        queryset =  Project.objects.all()
        return render(request, self.mytemplate, {"context": json.dumps(context),'projects':queryset})

    def post(self, request, **kwargs):
        # print("post", request.POST)
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        print(id, pw)

        user = authenticate(username=id, password=pw)
        print(user)

        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            login(request, user)
            # Redirect to a success page.
            # return HttpResponseRedirect("/account/loggedin/")
            # queryset =  Project.objects.filter(users__username=user)
            return render(request, self.mytemplate)
        else:
            logout(request)
            return redirect("home")



class IndexView(BaseView):
    mytemplate = "lamiacarto/index.html"

    def get(self, request):
        context = {"mytext": "popo"}

        return render(request, self.mytemplate, {"context": json.dumps(context)})

    # def post(self, request, **kwargs):
    #     super()
