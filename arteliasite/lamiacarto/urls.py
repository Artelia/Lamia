from . import views
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", views.BaseView.as_view(), name="home"),
    path("index", views.IndexView.as_view(), name="index"),
    path("posts", views.PostViewSet.as_view(), name="posts"),
]

