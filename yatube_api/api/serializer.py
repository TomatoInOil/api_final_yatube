from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Group, Post


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей."""

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "posts")


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов."""

    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field="username",
    )
    group = serializers.SlugRelatedField(
        queryset=Group.objects.all(), slug_field="slug", required=False
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "pub_date",
            "author",
            "image",
            "group",
        )


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для групп постов."""

    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
