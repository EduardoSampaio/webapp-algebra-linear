
import time

import numpy as np
from .resultado import Resultado
class LU:

    def __init__(self):
        self.Am = None

    def fatoraLU(self,m):  
        U = np.copy(m)  
        n = np.shape(U)[0]  
        L = np.eye(n)  
        for j in np.arange(n-1):  
            for i in np.arange(j+1,n):  
                L[i,j] = U[i,j]/U[j,j]  
                for k in np.arange(j+1,n):  
                    U[i,k] = U[i,k] - L[i,j]*U[j,k]  
                U[i,j] = 0        
        return L, U

    def executar(self, m):
        ini = time.time()
        original,triangular = self.fatoraLU(m)
        solucao = []
        fim = time.time()
        strTime = 'Tempo de Execução {:0.3f}'.format(fim-ini)
        resultado = Resultado(original, triangular, solucao, strTime)
        return resultado
# if __name__ == "__main__":
#     A = [[1, 2, -4, -4],
#         [2, 5, -9, -10],
#         [3, -2, 3, 11]]

#     lu = LU()
#     lu.fatoraLU(A)