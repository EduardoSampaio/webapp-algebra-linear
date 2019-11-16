
import time
from .resultado import Resultado

class GaussJordan:

    def __init__(self):
        self.m = None

    def gaussjordan(self, m):
        nLinhas = len(m)
        nColunas = len(m[0])
        print(nLinhas, nColunas)
        i = 0
        while(i < nLinhas):
            if(m[i][i] == 0):
                if(self.trocaLinhas(m, i)):
                    print("escalonar")
                else:
                    print("não é possível resolver o sistema")
            # imprimir(m)
            self.zerarInf(m, i)
            i = i+1
        i = i-1
        # print("inferior completa i: ",i)
        # imprimir(m)
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
            # imprimir(m)
            while(y < nColunas):
                m[x][y] = (m[i][y]*mult)+m[x][y]
                y = y+1
            x = x+1

    def zerarSup(self, m, i):
        # nLinhas = len(m)
        nColunas = len(m[0])
        p = i-1
        while(p >= 0):
            mult = m[p][i]
            x = i
            while(x < nColunas):
                m[p][x] = m[p][x] - (mult * m[i][x])
                x = x+1
            p = p - 1

    def resolver(self, m):
        n = len(m)
        x = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            x[i] = m[i][n]/m[i][i]
            for k in range(i-1, -1, -1):
                m[k][n] -= m[k][i] * x[i]
        return x

    def executar(self, m):
        ini = time.time()
        original = m.copy()
        triangular = self.gaussjordan(m)
        solucao = self.resolver(m)
        fim = time.time()
        strTime = 'Tempo de Execução {:0.3f}'.format(fim-ini)
        resultado = Resultado(original, triangular, solucao, strTime)
        return resultado


if __name__ == "__main__":
    matriz = [[1, 2, -4, -4],
              [2, 5, -9, -10],
              [3, -2, 3, 11]]

    g = GaussJordan()
    print(g.executar(matriz))
