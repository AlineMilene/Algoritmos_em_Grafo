# Descrição
# Faça um programa que leia um grafo ponderado e calcule um corte mínimo: você pode usar o algoritmo de Ford-Fulkerson para calcular o fluxo máximo de um vértice s até um vértice t.

# Entrada
# Recebe n, m, s e t; n é o total de vértices, m o total de arcos, s é a fonte e t é o sumidouro.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime a matriz de fluxo e a matriz de adjacência da rede residual, obtidas pelo algoritmo de Ford-Fulkerson.
# Finalmente, imprime o valor da capacidade de um corte mínimo e uma matriz de adjacência para indicar quais arcos pertencem ao corte mínimo encontrado.

import copy

# Função para calcular as listas de adjacência a partir da matriz de adjacência
def calculaListasAdjacencia(matrizAdj, n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            peso = matrizAdj[i][j]
            if peso > 0:  # Só adiciona se houver arco
                adj[i].append([j, peso])
    return adj

# Funções para manipular a fila (usada na BFS)
def insere(Q, x):
    Q.append(x)

def remove(Q):
    return Q.pop(0)

def vazio(Q):
    return len(Q) == 0

# Função BFS (Busca em Largura) para encontrar os vértices atingíveis
def bfs(matrizAdj, n, s):
    adj = calculaListasAdjacencia(matrizAdj, n)
    
    NIL = -1
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    
    pi = [NIL] * n  # Predecessores
    cor = [0] * n  # Cor dos vértices (para BFS)
    
    for v in range(n):
        cor[v] = BRANCO  # Marca todos os vértices como BRANCO
    cor[s] = CINZA  # Marca o vértice de origem como CINZA
    
    Q = []
    insere(Q, s)  # Insere o vértice de origem na fila
    
    atingiveis = [0] * n  # Inicializa a lista de vértices atingíveis
    # Executa a BFS
    while not vazio(Q):
        u = remove(Q)
        atingiveis[u] = 1  # Marca o vértice como atingível
        for v, peso in adj[u]:
            if cor[v] == BRANCO:  # Se o vértice ainda não foi visitado
                pi[v] = u
                cor[v] = CINZA
                insere(Q, v)
        cor[u] = PRETO  # Marca o vértice u como PRETO, visitado
    
    return pi, atingiveis

# Função que encontra o caminho aumentante e sua capacidade
def caminhoAumentante(matrizAdj, n, s, t):
    pi = bfs(matrizAdj, n, s)[0]
    
    NIL = -1
    INF = 999999  # Valor infinito
    capacidadeAumentante = INF
    j = t
    P = []
    
    while pi[j] != NIL:
        i = pi[j]
        peso = matrizAdj[i][j]
        P.insert(0, [i, j, peso])  # Insere no início da lista do caminho
        capacidadeAumentante = min(capacidadeAumentante, peso)  # Atualiza a capacidade mínima
        j = i
    
    if capacidadeAumentante == INF:
        capacidadeAumentante = 0  # Não encontrou caminho aumentante
    
    return P, capacidadeAumentante

# Função para aumentar o fluxo e atualizar a rede residual
def aumentaFluxo(matrizAdj, fluxo, P, capacidadeAumentante, n):
    for i, j, peso in P:
        if matrizAdj[i][j] > 0:
            fluxo[i][j] += capacidadeAumentante
        else:
            fluxo[i][j] -= capacidadeAumentante

    matrizAdjResidual = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            matrizAdjResidual[i][j] = matrizAdj[i][j]

    for i in range(n):
        for j in range(n):
            if fluxo[i][j] > 0:
                matrizAdjResidual[j][i] = fluxo[i][j]
                matrizAdjResidual[i][j] = matrizAdj[i][j] - fluxo[i][j]

    return fluxo, matrizAdjResidual

# Função Ford-Fulkerson
def fordFulkerson(matrizAdj, n, s, t):
    fluxo = [[0 for _ in range(n)] for _ in range(n)]  # Fluxo inicial é zero
    matrizAdjResidual = copy.deepcopy(matrizAdj)  # Inicializa a rede residual igual ao grafo de entrada
    
    # Encontra o primeiro caminho aumentante
    caminho, capacidadeAumentante = caminhoAumentante(matrizAdjResidual, n, s, t)
    
    # Enquanto houver caminho aumentante, aumenta o fluxo
    while capacidadeAumentante > 0:
        fluxo, matrizAdjResidual = aumentaFluxo(matrizAdj, fluxo, caminho, capacidadeAumentante, n)
        caminho, capacidadeAumentante = caminhoAumentante(matrizAdjResidual, n, s, t)
    
    return fluxo, matrizAdjResidual

# Função para calcular o corte mínimo
def calcularCorteMinimo(matrizAdj, matrizAdjResidual, n, s):
    # Busca em largura para encontrar os vértices atingíveis
    pi, atingiveis = bfs(matrizAdjResidual, n, s)
    
    # Calcula a matriz de corte mínimo
    matrizCorte = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            if matrizAdj[i][j] > 0 and atingiveis[i] != atingiveis[j]:
                matrizCorte[i][j] = 1
    
    # Calcula a capacidade do corte mínimo
    soma = 0
    for i in range(n):
        for j in range(n):
            if matrizCorte[i][j] > 0 and atingiveis[i] and not atingiveis[j]:
                soma += matrizAdj[i][j]
    
    return matrizCorte, soma

# Função principal
def main():
    # Lê os dados de entrada
    n, m, s, t = map(int, input().split())
    matrizAdj = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        matrizAdj[u][v] = w  # Atribui a capacidade do arco
    
    # Chama o algoritmo de Ford-Fulkerson
    fluxo, matrizAdjResidual = fordFulkerson(matrizAdj, n, s, t)
    
    # Imprime a matriz de fluxo
    print(fluxo)
    
    # Imprime a matriz de adjacência da rede residual
    print(matrizAdjResidual)
    
    # Calcula o valor do fluxo máximo (soma dos fluxos que chegam ao sumidouro)
    soma = sum(fluxo[i][t] for i in range(n))
    print(soma)
    
    # Calcula o corte mínimo
    matrizCorte, capacidadeCorte = calcularCorteMinimo(matrizAdj, matrizAdjResidual, n, s)
    
    # Imprime a matriz de corte mínimo
    print(matrizCorte)
    
if __name__ == '__main__':
    main()
