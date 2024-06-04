# Integrante - 1: Caio Henrique Gonçalves Seniuk
# Integrante - 2: Enzo Volpato

import time,math
import numpy as np
 
#USANDO A BIBLIOTECA NUMPY PARA CONVERTER ESSA LISTA EM UMA MATRIZ
matrizA = np.array([[2,1,5], [-1,3,-2]])
matrizB = np.array([[1,2], [-2,4], [2,5]])
matrizA_Transposta = []

#VARIÁVEIS DE APOIO
num_linhas = len(matrizA)
#CONTARÁ O NÚMERO DE COLUNAS, INDICE [0] É A LISTA = [2,1,5], CONTARÁ A QUANTIDADE DE ELEMENTOS DENTRO DESTA LISTA, QUE SÃO AS COLUNAS DA MATRIZ A
num_colunas = len(matrizA[0])

#LOOPING PARA PREENCHER A MATRIZ TRANSPOSTA COM LINHASxCOLUNAS DESEJADAS
for i in range(num_colunas):
    matrizA_Transposta.append([0]*num_linhas)

#LOOPING PARA ARMAZENAR NAS COLUNAS OS NUMEROS QUE ESTÃO EM LINHAS NA MATRIZ A
for i in range(num_linhas):
    for j in range(num_colunas):
        matrizA_Transposta[j][i] = matrizA[i][j]

#IMPRIMIR OS RESULTADOS
print("\nMatriz A:\n")
for l in range(0,2):
    for c in range(0,3):
        print(f"[{matrizA[l][c]:^5}]", end="")
    print()
print("\n")

print("Resultado da Matriz Transposta de A:\n")
for l in range(0,3):
    for c in range(0,2):
        print(f"[{matrizA_Transposta[l][c]:^5}]", end='')
    print()
print("\n")

print("Matriz B:\n")
for l in range(0,3):
    for c in range(0,2):
        print(f"[{matrizB[l][c]:^5}]", end='')
    print()
print("\n")

#ATRAVÉS DO NUMPY, FICA MAIS FÁCIL CALCULAR A SOMA DE MATRIZES
print(f"\nMatriz A Transposta + Matriz B: \n\n{matrizA_Transposta + matrizB}")