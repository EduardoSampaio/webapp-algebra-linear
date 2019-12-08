
import time
import timeit

from .resultado import Resultado
from .matrizIncompativelError import MatrizIncompativelError


class Gauss:

    def __init__(self):
        self.m = None

    def gauss(self, m):
        nLinhas = len(m)
        i = 0
        while(i < nLinhas):
            if (m[i][i] == 0):
                if self.trocaLinhas(m, i) or self.sistemaImpossivel(m):
                    raise MatrizIncompativelError(
                        'sistema impossível de resolver!')
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
            while(y < nColunas):
                m[x][y] = (m[i][y]*mult)+m[x][y]
                y = y+1
            x = x+1

    def resolver(self, m):
        n = len(m)
        x = [0 for i in range(n)] 
        fx = ''
        for i in range(n - 1, -1, -1):
            if m[i][i] == 0:
                x[i] = 0
                fx = 'x_' +str(i + 1)
                continue
            x[i] = m[i][n] / m[i][i]
            for k in range(i-1, -1, -1):
                m[k][n] -= m[k][i] * x[i]

        #formatar saída
        resultado = '\('
        for i in range(len(x)):
            if fx != '' and fx != 'x_' + str(i + 1):
                resultado += '\ x_' + str(i + 1) + '= ' + str(x[i]) + '+' + fx
            elif fx == 'x_' + str(i + 1):
                 resultado += '\ x_' + str(i + 1) + '= ' + fx
            else:    
                resultado += '\ x_' + str(i + 1) + '= ' + str(x[i])
        resultado += '\)'

        return resultado

    def executar(self, m):
        ini = time.time()
        original = m.copy()
        triangular = self.gauss(m)
        solucao = self.resolver(m)
        fim = time.time()
        strTime = 'Tempo de Execução: {:0.3f}'.format(fim-ini)
        resultado = Resultado(original, triangular, solucao, strTime)
        return resultado

    def linhaNula(self, m):
        linhas = len(m)
        colunas = len(m[0])

        for i in range(linhas - 1, linhas):
            for j in range(colunas-1):
                if m[i][j] != 0:
                    return False
        return True
    
    def sistemaImpossivel(self, m):
        linhas = len(m)
        colunas = len(m[0])

        for i in range(linhas - 1, linhas):
            for j in range(colunas):
                if m[i][j] == 0 and m[i][colunas-1] != 0:
                    return True
        return False

