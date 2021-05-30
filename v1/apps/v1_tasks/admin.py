from django.contrib import admin

# Register your models here.
from v1.apps.v1_tasks.models import Task

admin.site.register(Task)
