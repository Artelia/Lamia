from . import views
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.LamiaReportView.as_view(), name="lamiaprojectreport"),
    path(
        "<int:project_id>", views.LamiaReportView.as_view(), name="lamiaprojectreport",
    ),
]

