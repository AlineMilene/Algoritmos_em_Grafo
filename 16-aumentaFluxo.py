# Descrição
# Faça um programa que leia um grafo ponderado e dois vértices, s e t.
# Calcule o primeiro caminho aumentante de um vértice s até um vértice t, usando uma busca em largura (BFS).
# Calcule o resultado do primeiro aumento de fluxo, usando o caminho aumentante encontrado.
# (Considere o fluxo inicial zero.)

# Entrada
# Recebe n, m, s e t; n é o total de vértices, m o total de arcos, s é a fonte e t é o sumidouro.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Linha 1: imprima o caminho aumentante.
# (O formato do caminho é i, j, peso.)
# Linha 2: imprima a capacidade deste caminho.
# Imprima também o resultado de aumentar o fluxo com este caminho aumentante:
# Linha 3:  imprima a "matriz de fluxo".
# Linha 4: imprima a matriz de adjacência da rede residual resultante (após o aumento do fluxo).

# Função para calcular as listas de adjacência a partir da matriz de adjacência
def calculaListasAdjacencia(matrizAdj, n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            peso = matrizAdj[i][j]
            if peso > 0:
                adj[i].append([j, peso])
    return adj

# Função para inserir um elemento na fila
def insere(Q, x):
    Q.append(x)

# Função para remover um elemento da fila
def remove(Q):
    return Q.pop(0)

# Função para verificar se a fila está vazia
def vazio(Q):
    return len(Q) == 0

# Função BFS para calcular o caminho aumentante e a capacidade
def bfs(matrizAdj, n, s):
    adj = calculaListasAdjacencia(matrizAdj, n)
    NIL = -1
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    pi = [NIL] * n
    cor = [BRANCO] * n
    cor[s] = CINZA
    Q = []
    insere(Q, s)
    
    while not vazio(Q):
        u = remove(Q)
        for v, peso in adj[u]:
            if cor[v] == BRANCO:
                pi[v] = u
                cor[v] = CINZA
                insere(Q, v)
        cor[u] = PRETO

    return pi

# Função para obter o caminho aumentante e a capacidade
def caminhoAumentante(matrizAdj, n, s, t):
    pi = bfs(matrizAdj, n, s)
    INF = 999999
    capacidadeAumentante = INF
    j = t
    P = []
    
    while pi[j] != -1:
        i = pi[j]
        peso = matrizAdj[i][j]
        P.insert(0, [i, j, peso])  # Insere no início da lista
        capacidadeAumentante = min(capacidadeAumentante, peso)
        j = i

    if capacidadeAumentante == INF:
        capacidadeAumentante = 0

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

# Função principal
def main():
    # Leitura dos dados de entrada
    n, m, s, t = map(int, input().split())
    
    # Criação da matriz de adjacência com zeros
    matrizAdj = [[0 for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        i, j, peso = map(int, input().split())
        matrizAdj[i][j] = peso
    
    # Inicializando o fluxo com 0
    fluxo = [[0 for _ in range(n)] for _ in range(n)]

    # Encontrando o caminho aumentante
    P, capacidadeAumentante = caminhoAumentante(matrizAdj, n, s, t)
    
    # Imprimindo o caminho aumentante e a capacidade
    print(P)
    print(capacidadeAumentante)

    # Aumentando o fluxo
    fluxo, matrizAdjResidual = aumentaFluxo(matrizAdj, fluxo, P, capacidadeAumentante, n)
    
    # Imprimindo o fluxo e a matriz de adjacência residual
    print(fluxo)
    print(matrizAdjResidual)

    # Calculando o próximo caminho aumentante
    P, capacidadeAumentante = caminhoAumentante(matrizAdjResidual, n, s, t)
    
    # Imprimindo o próximo caminho aumentante e a capacidade
    print(P)
    print(capacidadeAumentante)

    # Aumentando o fluxo novamente
    fluxo, matrizAdjResidual = aumentaFluxo(matrizAdj, fluxo, P, capacidadeAumentante, n)
    
    # Imprimindo o fluxo final e a matriz residual final
    print(fluxo)
    print(matrizAdjResidual)

# Chamada da função principal
if __name__ == "__main__":
    main()
