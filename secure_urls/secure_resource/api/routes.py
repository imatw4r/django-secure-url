from rest_framework.routers import SimpleRouter

import secure_resource.api.views as views

router = SimpleRouter()
router.register("url", views.SecureUrlViewSet)
router.register("file", views.SecureFileViewSet)
router.register(
    "file/redirect",
    views.FileRedirectRetrieveModelViewSet,
)
router.register("url/redirect", views.UrlRedirectRetrieveModelViewSet)
router.register("stats/overall", views.ElementRedirectListStatisticsViewSet)
