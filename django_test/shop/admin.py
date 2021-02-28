from django.contrib import admin

from .models import Order
admin.site.register(Order)

from .models import Goods
admin.site.register(Goods)

