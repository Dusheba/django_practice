from django.contrib import admin

# Register your models here.
from v1.apps.v1_lessons.models import Lesson

admin.site.register(Lesson)
