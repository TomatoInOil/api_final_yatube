from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

API_VERSION = "v1"

app_name = "api"

urlpatterns = [
    path(
        f"{API_VERSION}/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        f"{API_VERSION}/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
