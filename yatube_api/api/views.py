from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Group, Post
from api.mixins import CreateListViewSet
from api.permissions import OnlyAuthorsUpdateDelete
from api.serializer import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
    UserSerializer,
)

User = get_user_model()


class PostViewSet(ModelViewSet):
    """CRUD для постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OnlyAuthorsUpdateDelete,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Только чтение информации о группах постов."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    """CRUD для комментариев к постам."""

    serializer_class = CommentSerializer
    permission_classes = (OnlyAuthorsUpdateDelete,)

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, pk=self.kwargs.get("post_id")),
        )


class FollowViewSet(CreateListViewSet):
    """Чтение подписок и создание одной из."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ("user__username", "following__username")

    def get_queryset(self):
        user = self.request.user
        queryset = user.follower.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    """Только чтение информации о пользователях."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
