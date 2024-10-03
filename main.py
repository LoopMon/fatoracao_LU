from time import time

def exibirMatrizQuadrada(matriz):
    tamMatriz = len(matriz)
    for i in range(tamMatriz):
        for j in range(tamMatriz):
            print(f'{matriz[i][j]:^7.2f}', end=" ")
        print("")

# Para ajudar a calcular o tempo de execução
start_time = time()

# vetores e matrizes do programa
matrizA = []
matrizB = []
x = []
y = []
l = []
aux = []

dimMatriz = int(input("Informe a dimensão da matriz: "))

# A partir da dimensão informada:
#   - matrizA vai ter o número de linhas igual a dimMatriz (cada linha é um vetor)
#   - vetor X vai ter o número de linhas igual a dimMatriz
for i in range(dimMatriz):
    matrizA.append([])
    x.append(0)


print(f"{' LEITURA MATRIZES':=^30}")
print("-= Informe a Matriz A:")
for i in range(0, dimMatriz):
    for j in range(0, dimMatriz):
        coeficiente = int(input(f"coeficiente a{i+1}{j+1}: "))
        matrizA[i].append(coeficiente)

        aux.append(0)
    # preenchendo matriz L para ter a mesma dimensão da matrizA
    l.append(aux[:])
    aux = []

print("\n-= Informe a Matriz B:")
for i in range(0, dimMatriz):
    valor = int(input(f"valor de a{i+1}{j+1}: "))
    matrizB.append(valor)


print("\nMatriz A:")
exibirMatrizQuadrada(matrizA)

# transformação matriz p/ triangular superior
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

# Criar matriz L
# Preenchar diagonal principal (1) e area triangular (0)
for i in range(0, dimMatriz):
    for j in range(0, dimMatriz):
        if i == j:
            l[i][j] = 1
        elif j > i:
            l[i][j] = 0

#Ly = b
y.append(matrizB[0])
resultado = 0
for i in range(1, dimMatriz):
    for j in range(0, i):
        resultado += l[i][j] * y[j]
    y.append(matrizB[i] - resultado)
    resultado = 0

#Ux = y
x[len(x)-1] = y[len(y)-1] / matrizA[dimMatriz-1][dimMatriz-1]
for i in range(dimMatriz-2, -1, -1):
    for j in range(dimMatriz-1, i-1, -1):
        resultado += matrizA[i][j] * x[j]
    x[i] = (y[i] - resultado) / matrizA[i][j]
    resultado = 0

print("Matriz U:")
exibirMatrizQuadrada(matrizA)
print("Matriz L:")
exibirMatrizQuadrada(l)

print("\nMatriz Y:")
for i in range(0, dimMatriz):
    print(f'{y[i]:^7.2f}', end=" ")

print("\nMatriz X:")
for i in range(0, dimMatriz):
    print(f'{x[i]:^7.2f}', end=" ")

print("\n\nTempo de execução:")
end_time = time()
execution_time = end_time - start_time
print(f'{execution_time = :.6f}')
