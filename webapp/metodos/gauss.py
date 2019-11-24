
import time

from .resultado import Resultado
from .matrizIncompativelError import MatrizIncompativelError

class Gauss:

    def __init__(self):
        self.m = None

    def gauss(self, m):
        nLinhas = len(m)
        # print(nLinhas,nColunas)
        i = 0
        while(i < nLinhas):
            if(m[i][i] == 0):
                if(not self.trocaLinhas(m, i)):
                    raise MatrizIncompativelError(
                        'não é possível resolver o sistema')                  
            #self.imprimir(m)
            self.zerar(m, i)
            i = i+1
        return m

    def trocaLinhas(self, m, i):
        x = i+1
        nLinhas = len(m)
        while(x < nLinhas):
            if(m[x][x] != 0):
                m[i], m[x] = m[x], m[i]
                return True
        return False

    def zerar(self, m, i):
        nLinhas = len(m)
        nColunas = len(m[0])
        x = i+1
        while(x < nLinhas):
            mult = -m[x][i]/m[i][i]
            m[x][i] = (m[i][i]*mult)+m[x][i]
            y = i+1
            #self.imprimir(m)
            while(y < nColunas):
                m[x][y] = (m[i][y]*mult)+m[x][y]
                y = y+1
            x = x+1

    def imprimir(self, m):
        for i in range(len(m)):
            print(m[i])
        print("\n")

    def resolver(self, m):
        n = len(m)
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = m[i][n]/m[i][i]
            for k in range(i-1, -1, -1):
                m[k][n] -= m[k][i] * x[i]
        #print(x)
        return x

    def executar(self, m):
        ini = time.time()
        original = m.copy()
        triangular = self.gauss(m)
        solucao = self.resolver(m)
        fim = time.time()
        strTime = 'Tempo de Execução: {:0.3f}'.format(fim-ini)
        resultado = Resultado(original, triangular, solucao, strTime)
        return resultado