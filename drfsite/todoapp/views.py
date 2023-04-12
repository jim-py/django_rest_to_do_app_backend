from .models import Task
from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task, List
from .serializers import TaskSerializer, ListSerializer


class TaskAPIView(APIView):
    def get(self, request):
        task = Task.objects.all()
        return Response({'posts': TaskSerializer(task, many=True).data})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'PUT not allowed'})

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = TaskSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'DELETE not allowed'})

        try:
            Task.objects.get(pk=pk).delete()
        except:
            return Response({'error': 'Object does not exist'})

        return Response({'post': 'delete post' + str(pk)})


class ListAPIView(APIView):
    def get(self, request):
        list = List.objects.all()
        return Response({'posts': ListSerializer(list, many=True).data})

    def post(self, request):
        serializer = ListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'PUT not allowed'})

        try:
            instance = List.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = ListSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'DELETE not allowed'})

        try:
            List.objects.get(pk=pk).delete()
        except:
            return Response({'error': 'Object does not exist'})

        return Response({'post': 'delete post ' + str(pk)})
