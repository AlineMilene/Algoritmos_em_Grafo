# Descrição
# Faça um programa que faz a leitura de um grafo ponderado e um vértice inicial.
# O programa deve imprimir na tela os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Entrada
# Recebe n, m e s; n é o total de vértices, m o total de arcos e s é o vértice inicial.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime os caminhos mínimos obtidos pelo algoritmo de Dijkstra.

# Função para verificar se ainda há vértices na fila de prioridade
def vazio(Q):
    return all(q == 0 for q in Q)

# Função para extrair o índice do vértice com a menor distância
def extraiMinimo(Q, d):
    min_dist = float('inf')
    min_index = -1
    for i in range(len(Q)):
        if Q[i] == 1 and d[i] < min_dist:
            min_dist = d[i]
            min_index = i
    Q[min_index] = 0  # Remove da fila
    return min_index

# Função principal para ler o grafo e aplicar o algoritmo de Dijkstra
def dijkstra():
    # Leitura dos dados de entrada
    n, m, s = (int(tmp) for tmp in input().split(" "))
    
    # Cria matriz de adjacência com zeros
    matrizAdj = [[0 for col in range(n)] for row in range(n)]
    
    # Leitura dos arcos
    for _ in range(m):
        i, j, peso = (int(tmp) for tmp in input().split(" "))
        matrizAdj[i][j] = peso

    # Inicialização
    INF = float('inf')
    NIL = -1
    d = [INF] * n
    pi = [NIL] * n
    d[s] = 0
    Q = [1] * n  # Todos os vértices na fila de prioridade

    while not vazio(Q):
        u = extraiMinimo(Q, d)
        for v in range(n):
            weight = matrizAdj[u][v]
            if weight > 0:  # Se existe um arco
                # Relax (u, v, w)
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    pi[v] = u

    # Impressão dos resultados
    print(d)
    print(pi)

# Chama a função principal
dijkstra()