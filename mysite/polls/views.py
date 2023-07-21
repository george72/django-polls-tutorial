from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola Mundo!!!!. Estás en el index del tutorial de Polls de Django")