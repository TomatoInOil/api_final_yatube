from typing import Sequence

from rest_framework import serializers


class FieldsAreNotEqual:
    """Проверка: 2 поля не равны между собой."""

    def __init__(self, fields: Sequence[str]) -> None:
        self.fields = fields

    def __call__(self, attrs):
        first_field, second_field = self.fields
        if attrs.get(first_field) == attrs.get(second_field):
            message = f"Поле {first_field} совпадает с {second_field}."
            raise serializers.ValidationError(message)
