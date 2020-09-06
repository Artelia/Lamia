from django.shortcuts import render, redirect
from django.views.generic import View
from artelialogin.models import User, Project
from django.contrib.auth import authenticate, login, logout
import logging, json

# Create your views here.


class BaseView(View):
    mytemplate = "artelialogin/artelialogin.html"

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
