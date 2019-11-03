

from .models import ManipularArquivo
from django.http import HttpResponse
from django.shortcuts import redirect, render

import numpy as np;
import csv
import io

def index(request):
    if request.method == 'POST':
        try:
            data = request.FILES['file'].read().decode('UTF-8')
            io_string = io.StringIO(data)         
            next(io_string)
            matriz = np.loadtxt(io_string, delimiter=',', dtype=int)
            return render(request, 'index.html', {'matriz': matriz})
        except:
            print("ERRO")
      
    return render(request, 'index.html')


