from . import views
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
# router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("lamiaapi/<int:project_id>", views.LamiaApiView.as_view(), name="lamiaapi",),
    path(
        "lamiaapi/<int:project_id>/<path:tablename>",
        views.LamiaApiView.as_view(),
        name="lamiaapi",
    ),
    path("media/<path:mediafile>", views.LamiaMedia.as_view(), name="lamiamedia",),
    path("qgisserver/<int:project_id>", views.LamiaGeoServer.as_view(), name="lamiaqgisserver",),
    path("qgisserver/<int:project_id>/<path:restrequest>", views.LamiaGeoServer.as_view(), name="lamiaqgisserver",),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

