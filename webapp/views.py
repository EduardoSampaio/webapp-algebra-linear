
import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if request.method == "POST":
        csv_file = request.FILES["docfile"]
        reader = csv.reader(csv_file)
        #read_file(reader)
        return redirect("")
    return render(request, 'index.html')


def read_file(reader):
    for row in reader:
        print(row)
