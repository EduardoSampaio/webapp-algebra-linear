
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from webapp.metodos.gauss import Gauss
from webapp.metodos.gaussjordan import GaussJordan
from webapp.metodos.matrizIncompativelError import MatrizIncompativelError
from django.urls import reverse


import numpy as np
import csv
import io


def index(request):
    return render(request, 'index.html')


def gauss(request):
    if request.method == 'POST':
        try:
            g = Gauss()
            matriz = readCSV(request)          
            resultado = g.executar(matriz)
            return render(request, 'gauss.html', {'resultado': resultado})
        except MatrizIncompativelError as e:
            return render(request, 'gauss.html', {'msg': str(e)})
    return render(request, 'gauss.html')


def gaussjordan(request):
    if request.method == 'POST':
        try:
            g = GaussJordan()
            matriz = readCSV(request)
            pivo  = isPivoteamento(request)
            resultado = g.executar(matriz)
            return render(request, 'gaussjordan.html', {'resultado': resultado})
        except MatrizIncompativelError as e:
            return render(request, 'gaussjordan.html', {'msg': str(e)})
    return render(request, 'gaussjordan.html')


def fatoracaolu(request):
    return render(request, 'fatoracaolu.html')


def readCSV(request):
    data = request.FILES['file'].read().decode('UTF-8')
    io_string = io.StringIO(data)
    matriz = np.loadtxt(io_string, delimiter=',', dtype=int)
    return matriz

def isPivoteamento(request):
    if request.POST.get('pivoteamento', '') == 'on':
        return True
    else:
        return False