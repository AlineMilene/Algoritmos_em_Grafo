# Descrição
# Faça um programa que faz a leitura de um grafo ponderado.
# O programa deve imprimir na tela a matriz de distâncias e a matriz "PI" dos caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as distâncias e os caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

import numpy as np

# Função para o algoritmo de Floyd-Warshall
def floyd_warshall():
    # Leitura dos dados de entrada
    n, m = (int(tmp) for tmp in input().split(" "))
    
    INF = float('inf')
    # Cria matriz de adjacência com INF
    matrizAdj = [[INF for _ in range(n)] for _ in range(n)]
    # Diagonal principal com zeros
    for i in range(n):
        matrizAdj[i][i] = 0
    
    # Leitura dos arcos
    for _ in range(m):
        i, j, peso = (int(tmp) for tmp in input().split(" "))
        # Marca arco com o peso
        matrizAdj[i][j] = peso

    # Inicialização das matrizes de distâncias e predecessores
    d = [np.copy(matrizAdj), np.copy(matrizAdj)]
    NIL = -1
    tmp = [[NIL for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrizAdj[i][j] < INF:
                tmp[i][j] = i

    # Predecessores: diagonal principal com NIL
    for i in range(n):
        tmp[i][i] = NIL
    pi = [np.copy(tmp), np.copy(tmp)]

    # Aplicação do algoritmo de Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                d[k % 2][i][j] = d[(k - 1) % 2][i][j]
                pi[k % 2][i][j] = pi[(k - 1) % 2][i][j]
                if d[(k - 1) % 2][i][k - 1] + d[(k - 1) % 2][k - 1][j] < d[(k - 1) % 2][i][j]:
                    d[k % 2][i][j] = d[(k - 1) % 2][i][k - 1] + d[(k - 1) % 2][k - 1][j]
                    pi[k % 2][i][j] = pi[(k - 1) % 2][k - 1][j]

    # Impressão das matrizes de distâncias e predecessores
    print(d[k % 2])
    print(pi[k % 2])

# Chama a função principal
floyd_warshall()