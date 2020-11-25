from django.conf import settings

from rest_framework.routers import SimpleRouter, DefaultRouter

import secure_resource.api.views as views


if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register("url/", views.SecureUrlViewSet)
router.register("file/", views.SecureFileViewSet)
router.register(
    "file/redirect",
    views.FileRedirectRetrieveModelViewSet,
)
router.register("url/redirect", views.UrlRedirectRetrieveModelViewSet)
router.register("stats/overall", views.ElementRedirectListStatisticsViewSet)

app_name = "API"

urlpatterns = router.urls
