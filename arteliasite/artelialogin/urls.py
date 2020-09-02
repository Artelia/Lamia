from . import views
from django.urls import path


urlpatterns = [
    path("", views.BaseView.as_view(), name="home"),
]
