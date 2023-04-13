from rest_framework import serializers
from .models import Task, List, Importance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class ImportanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Importance
        fields = '__all__'
