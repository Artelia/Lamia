from . import views
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.LamiaProjectView.as_view(), name="lamiaprojectgis",),
    path("<int:project_id>", views.LamiaProjectView.as_view(), name="lamiaprojectgis",),
    path(
        "<int:project_id>/<path:tablename>",
        views.LamiaCartoAPIView.as_view(),
        name="lamiacartoapi",
    ),
    path("<path:conffile>", views.LamiaProjectView.as_view(), name="lamiaprojectgis",),
]



