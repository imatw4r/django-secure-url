from django.urls import path, include

import secure_resource.views as views

app_name = "resources"

urlpatterns = [
    path(
        "element/file/create", views.SecureFileCreateView.as_view(), name="file-create"
    ),
    path("element/url/create", views.SecureUrlCreateView.as_view(), name="url-create"),
    path(
        "element/detail/<int:pk>",
        views.SecureElementDetailView.as_view(),
        name="element-detail",
    ),
    path(
        "element/redirect/<int:pk>",
        views.redirect_element_view,
        name="element-redirect",
    ),
]
