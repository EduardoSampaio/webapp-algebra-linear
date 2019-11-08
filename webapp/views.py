

from .models import ManipularArquivo
from django.http import HttpResponse
from django.shortcuts import redirect, render

import numpy as np
import csv
import io


def index(request):
    if request.method == 'POST':
        matriz = readCSV(request)
        return render(request, 'index.html', {'matriz': matriz}) 
    return render(request, 'index.html')


def gauss(request):
    resultado = '$$x_{1}=1 x_{2}=5$$'
    return render(request, 'gauss.html', {'resultado':resultado})


def gaussjordan(request):
    return render(request, 'gaussjordan.html')

def fatoracaolu(request):
    return render(request, 'fatoracaolu.html')

def readCSV(request):
    data = request.FILES['file'].read().decode('UTF-8')
    io_string = io.StringIO(data)
    matriz = np.loadtxt(io_string, delimiter=',', dtype=int)
    return matriz
