from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def teste(request):
    return HttpResponse("Aula Dev 1")


def saudacao(request):
    hoje = datetime.now()
    if hoje.hour <= 12:
        mensagem = "Bom dia"
    elif 12 <= hoje.hour <= 10:
        mensagem = "Boa noite"
    else:
        mensagem = "boa noite"

    contexto = {
        "valor": mensagem
    }

    return render(request, "base.html", contexto)


def parametro(request, nome):
    nome = nome.upper()
    return HttpResponse(f"<h1> Boa noite {nome} </h1>")


def desafio(request, nome):
    return HttpResponse(f"<h1> Quantidade de letras: {len(nome)} </h1>")
