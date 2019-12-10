
import time
import copy

from .resultado import Resultado
from .matrizIncompativelError import MatrizIncompativelError


class GaussJordan:

    def __init__(self):
        self.m = None

    def gaussjordan(self, m):
        nLinhas = len(m)
        nColunas = len(m[0])
        i = 0
        while(i < nLinhas):
            if (m[i][i] == 0):
                self.trocaLinhas(m, i)
                if self.sistemaImpossivel(m):
                    raise MatrizIncompativelError(
                        'sistema impossível de resolver!')
                elif(self.linhaNula(m)):
                    raise MatrizIncompativelError(
                        'o sistema possui infinitas soluções!')
            self.zerarInf(m, i)
            i = i+1
        i = i-1
        while(i > 0):
            self.zerarSup(m, i)
            i = i-1
        return m

    def zerarInf(self, m, i):
        nLinhas = len(m)
        nColunas = len(m[0])
        x = i+1
        p = 0
        multd = 1/m[i][i]
        while(p < nColunas):
            m[i][p] = m[i][p]*multd
            p = p+1
        while(x < nLinhas):
            mult = -m[x][i]/m[i][i]
            m[x][i] = (m[i][i]*mult)+m[x][i]
            y = i+1
            while(y < nColunas):
                m[x][y] = (m[i][y]*mult)+m[x][y]
                y = y+1
            x = x+1

    def zerarSup(self, m, i):
        nColunas = len(m[0])
        p = i-1
        while(p >= 0):
            mult = m[p][i]
            x = i
            while(x < nColunas):
                m[p][x] = m[p][x] - (mult * m[i][x])
                x = x+1
            p = p - 1

    def trocaLinhas(self, m, i):
        x = i+1
        nLinhas = len(m)
        while(x < nLinhas):
            if(m[x][x] != 0):
                m[i], m[x] = m[x], m[i]
                return True
        return False

    def resolver(self, m):
        n = len(m)
        x = [0 for i in range(n)]
        fx = ''
        for i in range(n - 1, -1, -1):
            if m[i][i] == 0:
                x[i] = 0
                fx = 'x_' + str(i + 1)
                continue
            x[i] = m[i][n] / m[i][i]
            for k in range(i-1, -1, -1):
                m[k][n] -= m[k][i] * x[i]
        return self.formatar(x, fx)
        
    def formatar(self, x, fx):
        # formatar saída
        resultado = '\('
        for i in range(len(x)):
            if fx != '' and fx != 'x_' + str(i + 1):
                resultado += '\ x_' + str(i + 1) + \
                    '= ' + str("%.1f" % x[i]) + '+' + fx
            elif fx == 'x_' + str(i + 1):
                resultado += '\ x_' + str(i + 1) + '= ' + fx
            else:
                resultado += '\ x_' + str(i + 1) + '= ' + str("%.1f" % x[i])
        resultado += '\)'
        return resultado


    def executar(self, m):
        ini = time.time()
        original = copy.deepcopy(m)
        triangular = self.gaussjordan(m)
        triangular = copy.deepcopy(triangular)
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
