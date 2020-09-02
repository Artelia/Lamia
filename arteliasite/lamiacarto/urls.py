from . import views
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
# router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path(
        "lamiaproject/<int:project_id>",
        views.LamiaProjectView.as_view(),
        name="lamiaproject",
    ),
    path(
        "lamiaproject/<path:conffile>",
        views.LamiaProjectView.as_view(),
        name="lamiaproject",
    ),
    path("lamiaapi/<int:project_id>", views.LamiaApiView.as_view(), name="lamiaapi",),
    path(
        "lamiaapi/<int:project_id>/<path:tablename>",
        views.LamiaApiView.as_view(),
        name="lamiaapi",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

