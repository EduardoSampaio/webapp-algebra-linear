import codecs
import csv

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    if request.method == "POST":
        csv_file = request.FILES["arquivo"]
        reader = csv.reader(csv_file) 
        read_file(reader)
    return render(request, 'webapp/index.html')

def read_file(reader):
    for row in reader :
        print (row)