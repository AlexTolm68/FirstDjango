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
        item = Item.objects.get(pk=id_item)
        return render(request, "items.html",
                      {"name": item.name,
                       "brand": item.brand,
                       "description": item.description,
                       "count": item.count})
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id={id_item} не найден в БД")

    # return HttpResponseNotFound(f"Товар с id={id_item} не найден")


def list_items(request):
    items = Item.objects.all()
    return render(request, "items_list.html", {"goods": items})
