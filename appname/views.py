from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse("Беттин көркү нур мененБелдин көркү кур менен."
                        "Биз сүйгөн сулуу - Мөлмөлүм,Бүгүн белгилүү болсун ыр менен."
                        "Эки илабиң - кызыл гүл,Ачылгандай, Мөлмөлүм,"
                        "Бир карасам жүрөккө от,Чачылгандай, Мөлмөлүм.")