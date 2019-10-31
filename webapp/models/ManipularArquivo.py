import csv


class ManipularArquivo:

    def __init__(self, request):
        self.request = request

    def ler(self, request):
        csv_file = request.FILES["docfile"]
        reader = csv.reader(csv_file)
        return None
