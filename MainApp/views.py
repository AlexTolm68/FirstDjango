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

    text = f"Имя: {firstname}\nОтчество: {otchestvo}\nФамилия: {secondname}\nТелефон: {secondname}\nemail: {secondname}"
    return HttpResponse(text)
