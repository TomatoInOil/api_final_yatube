from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post
from api.validators import UserIsNotAuthor


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
        slug_field="username",
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False
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
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )

    class Meta:
        model = Follow
        fields = ("following", "user")
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=["user", "following"]
            ),
            UserIsNotAuthor(),
        ]
