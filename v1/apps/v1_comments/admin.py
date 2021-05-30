from django.contrib import admin

# Register your models here.
from v1.apps.v1_comments.models import Comment

admin.site.register(Comment)
