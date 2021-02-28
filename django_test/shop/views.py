from requests import Response

from django_test.shop.models import Order


def get_order(request, id_order):
    return Response(Order.objects.filter(id_order).get())


def del_order(request, id_order):
    Order.objects.filter(id_order).delete()
    return Response("")


def list_order(request):
    return Response(list(Order.objects.all()))
