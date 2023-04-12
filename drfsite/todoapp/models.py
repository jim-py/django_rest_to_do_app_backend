from django.db import models


class Task(models.Model):
    list = models.ForeignKey('List', on_delete=models.CASCADE, null=True)
    importance = models.ForeignKey('Importance', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)


class List(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)


class Importance(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    level = models.IntegerField()
