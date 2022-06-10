from django.urls import include, path
from rest_framework import routers

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet,
    UserViewSet,
)

API_VERSION = "v1"

router = routers.DefaultRouter()
router.register(r"^posts", PostViewSet, basename="posts")
router.register(r"^groups", GroupViewSet, basename="groups")
router.register(
    r"^posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
router.register(r"^users", UserViewSet, basename="users")
router.register(r"^follow", FollowViewSet, basename="follow")

app_name = "api"

urlpatterns = [
    path(f"{API_VERSION}/", include("djoser.urls")),
    path(f"{API_VERSION}/", include("djoser.urls.jwt")),
    path(f"{API_VERSION}/", include(router.urls)),
]
