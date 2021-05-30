from django.contrib import admin

# Register your models here.
from v1.apps.v1_courses.models import Course

admin.site.register(Course)
