from django.contrib import admin

# Register your models here.
from v1.apps.v1_users.models import User

admin.site.register(User)
