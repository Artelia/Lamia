from . import views
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", views.BaseView.as_view(), name="home"),
    # path("index", views.IndexView.as_view(), name="index"),
    path(
        "lamiaproject/<int:project_id>",
        views.LamiaProjectView.as_view(),
        name="lamiaproject",
    ),
    path("lamiaapi/<int:project_id>", views.PostViewSet.as_view(), name="lamiaapi",),
    path(
        "lamiaapi/<int:project_id>/<str:tablename>",
        views.PostViewSet.as_view(),
        name="lamiaapi",
    ),
    path("lamiafunc/<int:project_id>", views.LamiaFuncAPI.as_view(), name="lamiafunc",),
]

