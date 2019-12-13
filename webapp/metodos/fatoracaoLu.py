
import time

import numpy as np
from .resultado import Resultado


class LU:

    def __init__(self):
        self.Am = None

    def trocaLinhas(self, m, i):
        x = i+1
        nLinhas = len(m)
        while(x < nLinhas):
            if(m[x][x] != 0):
                m[i], m[x] = m[x], m[i]
                return True
        return False

    def removeVetor(self, m):
        nLinhas = len(m)
        nCols = len(m[0])
        b = []  # retirando o vetor b
        i = 0
        while(i < nLinhas):
            b.append(m[i].pop(nCols-1))
            i = i+1
        return b

    def LU(self, m):
        nLinhas = len(m)
        nCols = len(m[0])
        b = self.removeVetor(m)

        if(nLinhas > nCols):
            m = self.completar(m)
        # print(nLinhas,nColunas)
        i = 0
        ml = self.identidade(m)

        while(i < nLinhas):
            if(m[i][i] == 0):
                if(self.trocaLinhas(m, i)):
                    print("escalonar")
                else:
                    print("não é possível resolver o sistema")
                # imprimir(m)
            self.upper(m, ml, i)
            i = i+1

        # devolvendo o vetor b para a matriz
        i = 0
        while(i < len(ml)):
            ml[i].append(b[i])
            i = i+1

        y = self.resolverL(ml)
        i = 0
        while(i < len(m)):
            m[i].append(y[i])
            i = i+1

        # print("\n")
        # imprimir(m)

        self.resolverU(m)
        # imprimir(m)
        return m, ml  # m superior/ ml inferior

    def upper(self, m, ml, i):
        nLinhas = len(m)
        nColunas = len(m[0])
        x = i+1
        while(x < nLinhas):
            mult = -m[x][i]/m[i][i]
            # aqui começa a bagaça
            ml[x][i] = -mult
            m[x][i] = (m[i][i]*mult)+m[x][i]
            y = i+1
            while(y < nColunas):
                m[x][y] = (m[i][y]*mult)+m[x][y]
                y = y+1
            x = x+1
        return

    def identidade(self, m):
        nLinhas = len(m)
        nCols = len(m[0])
        a = [[0] * nCols for i in range(nLinhas)]
        for i in range(nLinhas):
            for j in range(nCols):
                if(i == j):
                    a[i][j] = 1
        return a

    def completar(self, m):
        nLinhas = len(m)
        nCol = len(m[0])
        m2 = [[0 for x in range(nLinhas)] for y in range(nLinhas)]
        i = 0
        j = 0
        while (i < nLinhas):
            j = 0
            while(j < nLinhas):
                if (j < nCol):
                    m2[i][j] = m[i][j]
                elif (i == j):
                    m2[i][j] = 1
                else:
                    m2[i][j] = 0
                j = j+1
            i = i+1
        return m2

    def resolverL(self, m):  # b é o vetor retirado da matriz no início
        n = len(m)
        y = [0 for i in range(n)]
        for i in range(n):
            y[i] = m[i][n] / m[i][i]
            for k in range(i):
                y[i] -= m[i][k] * y[k]
        return y

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

    def resolverU(self, m):
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

    def executar(self, m):
        ini = time.time()
        m = m.tolist()
        L, U = self.LU(m)
        solucao = self.resolverU(U)
        self.removeVetor(L)
        self.removeVetor(U)
    
        fim = time.time()
        strTime = 'Tempo de Execução {:0.3f}'.format(fim-ini)
        resultado = Resultado(L, U, solucao, strTime)
        return resultado
