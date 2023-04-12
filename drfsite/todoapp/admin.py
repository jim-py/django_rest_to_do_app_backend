from django.contrib import admin
from .models import Task, List, Importance

admin.site.register(Task)
admin.site.register(List)
admin.site.register(Importance)
