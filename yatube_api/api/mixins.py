from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """ViewSet, который позволяет создать объект и получить список объектов."""

    pass
