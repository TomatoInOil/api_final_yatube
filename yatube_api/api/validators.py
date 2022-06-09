from rest_framework import serializers


class UserIsNotAuthor:
    """Проверка: подписчик и автор - разные пользователи."""

    def __call__(self, attrs):
        if attrs.get("user") == attrs.get("following"):
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя."
            )
