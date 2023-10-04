from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    text = f"""<h1> "Изучаем django" </h1>
    <strong> Автор </strong >: <i> Шиховцев Вадим Викторович </i>"""
    return HttpResponse(text)


def about(request):
    firstname = "Александр"
    secondname = "Толмачев"
    otchestvo = "Владимирович"
    phone = "8-923-600-01-02"
    email = "av_tolm@mail.ru"

    text = f"""<h>Имя: {firstname}, Отчество: {otchestvo}, Фамилия: {secondname}, Телефон: {phone}, email: {email}</h>"""
    return HttpResponse(text)


items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель Фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124}
]


def get_items(request, id_item):
    try:
        for item in items:
            if item["id"] == id_item:
                name = item["name"]
                quantity = item["quantity"]
                break
        text = f"""<h> id: {id_item} name: {name} quantity: {quantity}</h>"""
    except UnboundLocalError:
        text = f"Товар с id={id_item} не найден"

    return HttpResponse(text)


def list_items(request):
    text = ""
    for item in items:
        id_item = item["id"]
        name = item["name"]
        quantity = item["quantity"]
        goods = f"""<h> id: {id_item} name: {name} quantity: {quantity}</h> <a href="/items/{id_item}">id:{id_item}</a>,  
        \n"""
        text += goods
    return HttpResponse(text)
