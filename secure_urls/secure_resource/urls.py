from django.urls import path, include

from secure_resource.api.routes import router
import secure_resource.views as views


urlpatterns = [
    path("", views.index, name="home"),
    path(
        "element/file/create/", views.SecureFileCreateView.as_view(), name="file-create"
    ),
    path("element/url/create/", views.SecureUrlCreateView.as_view(), name="url-create"),
    path(
        "element/redirect/<int:pk>/",
        views.redirect_element_view,
        name="element-redirect",
    ),
    path(
        "element/detail/<int:pk>/",
        views.SecureElementDetailView.as_view(),
        name="element-detail",
    ),
    path("api/", include("secure_resource.api_routes")),
]
