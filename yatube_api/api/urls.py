from django.urls import path, include

API_VERSION = "v1"

app_name = "api"

urlpatterns = [
    path(r"^auth/", include("djoser.urls")),
    path(r"^auth/", include("djoser.urls.jwt")),
]
