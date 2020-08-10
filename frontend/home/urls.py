from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("index/<id_projet>", views.index),
]
