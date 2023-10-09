from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    context = {"firstname": "Александр",
               "secondname": "Толмачев",
               "otchestvo": "Владимирович",
               "phone": "8-923-600-01-02",
               "email": "mail@mail.ru"}

    return render(request, "about.html", context)


# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 7, "name": "Картофель Фри", "quantity": 0},
#     {"id": 8, "name": "Кепка", "quantity": 124}
# ]


def get_items(request, id_item):

    try:
        item = Item.objects.get(id=id_item)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id={id_item} not found')
    else:
        context = {
            "item": item
        }
        return render(request, "items.html", context)


def list_items(request):
    items = Item.objects.all()
    return render(request, "items_list.html", {"goods": items})
