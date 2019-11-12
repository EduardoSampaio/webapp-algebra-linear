
from django.http import HttpResponse
from django.shortcuts import redirect, render
from webapp.metodos.gauss import Gauss


import numpy as np
import csv
import io


def index(request):
    if request.method == 'POST':
        matriz = readCSV(request)
        return render(request, 'index.html', {'matriz': matriz})
    return render(request, 'index.html')


def gauss(request):
    if request.method == 'POST':
        g = Gauss()
        matriz = readCSV(request)
        resultado = g.executar(matriz)
        matriz = readCSV(request)
        return render(request, 'gauss.html', {'resultado': resultado})
    return render(request, 'gauss.html')


def gaussjordan(request):
    return render(request, 'gaussjordan.html')


def fatoracaolu(request):
    return render(request, 'fatoracaolu.html')


def readCSV(request):
    data = request.FILES['file'].read().decode('UTF-8')
    io_string = io.StringIO(data)
    matriz = np.loadtxt(io_string, delimiter=',', dtype=int)
    return matriz
