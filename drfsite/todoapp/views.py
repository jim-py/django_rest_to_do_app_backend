from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from .models import Task, List, Importance
from .serializers import TaskSerializer, ListSerializer, ImportanceSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(mixins.CreateModelMixin,  # Создание объектов
                  mixins.RetrieveModelMixin,  # Просмотр одного объекта
                  mixins.UpdateModelMixin,  # Изменение объектов
                  mixins.ListModelMixin,  # Просмотр всех объектов
                  mixins.DestroyModelMixin,  # Удаление объектов
                  GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['id', 'importance', 'date']
    ordering = ['-id']
    filterset_fields = ['status', 'list']


class ListViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['id', 'name']
    ordering = ['-id']


class ImportanceViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Importance.objects.all()
    serializer_class = ImportanceSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['level']
    ordering = ['-level']
