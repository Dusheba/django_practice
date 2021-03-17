from django.http import JsonResponse

from shop.models import Order


def get_order(request, id_order):
    a = Order.objects.get(pk=id_order)
    get_id = {"id_order": a.id,
              "name": a.name,
              "date_created": a.date_created
              }

    return JsonResponse(get_id)


def del_order(request, id_order):
    a = Order.objects.get(pk=id_order)
    a.delete()
    return JsonResponse()


def list_order(request):
    get_id = []
    for a in Order.objects.all():
        get_id.append({"id_order": a.id,
                       "name": a.name,
                       "date_created": a.date_created
                       })

    return JsonResponse(get_id, safe=False)