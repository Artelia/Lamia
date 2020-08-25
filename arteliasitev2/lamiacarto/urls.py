from . import views
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

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
    # path("lamiafunc/<int:project_id>", views.LamiaFuncAPI.as_view(), name="lamiafunc",),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

