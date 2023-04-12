from rest_framework import serializers
from .models import Task, List


class TaskSerializer(serializers.Serializer):
    list_id = serializers.IntegerField()
    importance_id = serializers.IntegerField()
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.list_id = validated_data.get('list_id', instance.list_id)
        instance.importance_id = validated_data.get('importance_id', instance.importance_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class ListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    color = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return List.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
