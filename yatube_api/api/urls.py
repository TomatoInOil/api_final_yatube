from django.urls import path, include

API_VERSION = "v1"

app_name = "api"

urlpatterns = [
    path(f"{API_VERSION}/", include("djoser.urls")),
    path(f"{API_VERSION}/", include("djoser.urls.jwt")),
]
