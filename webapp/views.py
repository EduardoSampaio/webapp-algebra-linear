


from .models import ManipularArquivo
from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    if request.method == "POST":
       arquivo = ManipularArquivo(request)
       arquivo.ler()
    return render(request, 'index.html')
