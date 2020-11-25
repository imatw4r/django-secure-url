from django.conf import settings

from rest_framework.routers import DefaultRouter
import secure_resource.api.views as views

router = DefaultRouter(trailing_slash=False)

router.register("url", views.SecureUrlViewSet, basename="url-vs")
router.register("file", views.SecureFileViewSet, basename="file-vs")
router.register(
    "file/redirect",
    views.FileRedirectRetrieveModelViewSet,
    basename="file-redirect-vs",
)
router.register(
    "url/redirect", views.UrlRedirectRetrieveModelViewSet, basename="url-redirect-vs"
)
router.register(
    "stats/overall",
    views.ElementRedirectListStatisticsViewSet,
    basename="stats-overall-lvs",
)

app_name = "API"
urlpatterns = router.get_urls()
