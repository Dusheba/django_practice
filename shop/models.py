from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(verbose_name="Картинка")
    price = models.IntegerField(null=True, blank=True)


class Order(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    id_goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
