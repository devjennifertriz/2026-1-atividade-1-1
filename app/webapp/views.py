from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, Professor! Sou sua aluna Jennifer Nascimento em Sistemas Operacionais.")



# Create your views here.
