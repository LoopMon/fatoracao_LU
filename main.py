import pandas as pd
import numpy as np
from time import time

def exibirMatrizQuadrada(matriz):
    tamMatriz = len(matriz)
    for i in range(tamMatriz):
        for j in range(tamMatriz):
            print(f'{matriz[i][j]:^7.2f}', end=" ")
        print("")

# Para ajudar a calcular o tempo de execução
start_time = time()

# Ler os dados do arquivo Excel
arquivo_excel = 'dados.xlsx'  

# Leitura das planilhas do Excel 
#   - o arquivo deve ter 2 planilhas
#   - os nomes das planilhas devem ser A e B respectivamente
#   - planilha A: deve contar os coeficientes do sistema
#   - planilha B: deve conter os termos independentes do sistema em coluna
df_matrizA = pd.read_excel(arquivo_excel, sheet_name='A', header=None)
df_matrizB = pd.read_excel(arquivo_excel, sheet_name='B', header=None)

# DataFrames para arrays do NumPy
matrizA = df_matrizA.to_numpy()
matrizB = df_matrizB.to_numpy().flatten()  # vetor B como um array 1D

# Dimensão da matriz a partir da matriz A
dimMatriz = matrizA.shape[0]

# Inicializar vetores e matrizes necessários
x = np.zeros(dimMatriz)
y = []
l = np.zeros_like(matrizA, dtype=float)

print("\nMatriz A:")
exibirMatrizQuadrada(matrizA)

# Transformação da matriz para triangular superior (Fatoração LU)
i = 1
j = 0
cont = 0
pivo = matrizA[0][0]
pivoLinha = 0
while i < dimMatriz:
    # calcular o multiplicador de linha
    ml = matrizA[i][j] / pivo
    # adicionar ml na matriz L
    l[i][j] = ml
    # encontrar o pivo e sua linha
    if i == j:
        pivo = matrizA[i][j]
        pivoLinha = i
    # percorrer a linha a ser modificada
    while j < dimMatriz:
        matrizA[i][j] = matrizA[i][j] - ml * matrizA[pivoLinha][j]
        j += 1

    i += 1
    j = 0

    # fim de uma iteração
    if i >= dimMatriz:
        i -= 1
        j = i - 1
        pivo = matrizA[i-1][j]
        pivoLinha = i-1
        cont += 1
        # se o numero de iterações for igual a d - 1, encerra o loop
        if cont >= dimMatriz - 1:
            break

# Preencher diagonal principal de L com 1 e triangular superior com 0
for i in range(dimMatriz):
    for j in range(dimMatriz):
        if i == j:
            l[i][j] = 1
        elif j > i:
            l[i][j] = 0

# Resolver Ly = B
y.append(matrizB[0])
resultado = 0
for i in range(1, dimMatriz):
    for j in range(i):
        resultado += l[i][j] * y[j]
    y.append(matrizB[i] - resultado)
    resultado = 0

# Resolver Ux = y
x[dimMatriz-1] = y[dimMatriz-1] / matrizA[dimMatriz-1][dimMatriz-1]
for i in range(dimMatriz-2, -1, -1):
    for j in range(dimMatriz-1, i-1, -1):
        resultado += matrizA[i][j] * x[j]
    x[i] = (y[i] - resultado) / matrizA[i][i]
    resultado = 0

print("\nMatriz U:")
exibirMatrizQuadrada(matrizA)
print("\nMatriz L:")
exibirMatrizQuadrada(l)

print("\nMatriz Y:")
for i in range(dimMatriz):
    print(f'{y[i]:^7.2f}', end=" ")

print("\n\nMatriz X (solução do sistema):")
for i in range(dimMatriz):
    print(f'{x[i]:^7.2f}', end=" ")

# Exibir tempo de execução
end_time = time()
execution_time = end_time - start_time
print(f'\n\nTempo de execução: {execution_time:.6f} segundos')
