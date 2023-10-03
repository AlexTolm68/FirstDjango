from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    text = """< h1 > "Изучаем django" < / h1 >
    < strong > Автор < / strong >: < i > Иванов < / i > """
    return HttpResponse(text)


def about(request):
    firstname = "Александр"
    secondname = "Толмачев"
    otchestvo =  "Владимирович"
    phone = "8-923-600-01-02"
    email = "av_tolm@mail.ru"

    text = f"""<h1>Имя: {firstname} Отчество: {otchestvo} Фамилия: {secondname} Телефон: {phone} email: {email}</h1>"""
    return HttpResponse(text)

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель Фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124}
]

def item(request):

    return HttpResponse()


