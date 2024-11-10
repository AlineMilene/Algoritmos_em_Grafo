# Descrição
# Faça um programa que leia um grafo ponderado e calcule um caminho aumentante de um vértice s até um vértice t, usando uma busca em largura (BFS).

# Entrada
# Recebe n, m, s e t; n é o total de vértices, m o total de arcos, s é a fonte e t é o sumidouro.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime um caminho aumentante e a capacidade deste caminho.
# (O formato do caminho é i, j, peso.)

# Função que calcula as listas de adjacência a partir da matriz de adjacência
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

# Função que realiza a busca em largura (BFS) e retorna os predecessores
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
    
    # Executa a BFS
    while not vazio(Q):
        u = remove(Q)
        for v, peso in adj[u]:
            if cor[v] == BRANCO:  # Se o vértice ainda não foi visitado
                pi[v] = u
                cor[v] = CINZA
                insere(Q, v)
        cor[u] = PRETO  # Marca o vértice u como PRETO, visitado
    
    return pi

# Função que encontra o caminho aumentante e sua capacidade
def caminhoAumentante(matrizAdj, n, s, t):
    pi = bfs(matrizAdj, n, s)
    
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

# Função principal para ler os dados e chamar as funções auxiliares
def main():
    # Leitura dos dados de entrada
    n, m, s, t = map(int, input().split())
    
    # Criação da matriz de adjacência com valores iniciais
    matrizAdj = [[0 for _ in range(n)] for _ in range(n)]
    
    # Leitura das arestas e preenchimento da matriz de adjacência
    for _ in range(m):
        i, j, peso = map(int, input().split())
        matrizAdj[i][j] = peso
    
    # Chama a função para encontrar o caminho aumentante e sua capacidade
    P, capacidadeAumentante = caminhoAumentante(matrizAdj, n, s, t)
    
    # Exibe o caminho aumentante e a capacidade do caminho
    print(P)
    print(capacidadeAumentante)

# Executa o programa
if __name__ == "__main__":
    main()
