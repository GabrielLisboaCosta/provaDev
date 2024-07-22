from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from consultas.models import Paciente, Atendimento


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

    return render(request, "consultas/arquivo.html", contexto)


def parametro(request, nome):
    nome = nome.upper()
    return HttpResponse(f"<h1> Boa noite {nome} </h1>")


def desafio(request, nome):
    return HttpResponse(f"<h1> Quantidade de letras: {len(nome)} </h1>")


def paciente(request, id):
    p1 = Paciente.objects.get(pk=id)
    contexto = {
        "paciente": p1
    }

    return render(request, "consultas/paciente.html", contexto)


def list_pacientes(request):
    total = Paciente.objects.all()
    contexto = {
        "pacientes": total
    }
    return render(request, "consultas/pacientes.html", contexto)


def atendimento(request, id):
    a1 = Atendimento.objects.get(pk=id)
    contexto = {
        "atendimento": a1
    }

    return render(request, "consultas/atendimento.html", contexto)


def delete(request, paciente_id):
    paci = get_object_or_404(Paciente, pk=paciente_id)
    try:
        if request.method == 'POST':
            v_paciente_id = request.POST.get("paciente_id", None)
            if int(v_paciente_id) == paciente_id:
                paci.delete()
                return redirect('consultas:pacientes')
        else:
            contexto = {
                "paciente": paci,
            }
            return render(request, "consultas/delete_paciente.html", contexto)
    except Exception as e:
        contexto = {}
        print(e)
        return render(request, "consultas/pacientes.html", contexto)
