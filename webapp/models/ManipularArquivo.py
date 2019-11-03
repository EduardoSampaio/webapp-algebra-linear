import numpy as np
import csv
import io


class ManipularArquivo:

    def __init__(self,request):
        self.request = request

    def ler(self):
      data = self.request.FILES['file'].read().decode('UTF-8')
      io_string = io.StringIO(data)
      next(io_string)
      matriz = np.loadtxt(io_string, delimiter=',', dtype=int)
      return matriz
