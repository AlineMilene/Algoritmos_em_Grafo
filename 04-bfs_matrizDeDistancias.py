# Descricao
# Faça um programa que faz a leitura de um grafo e imprime a matriz de distâncias obtidas por buscas em largura (BFS).

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime a matriz de distâncias obtidas por buscas BFS.

# Solucao

# Funcoes auxiliares para gerenciamento da fila.
def insere(Q, x):
    Q.append(x)

def remove(Q):
    return Q.pop(0)

def vazio(Q):
    return len(Q) == 0

# Funcao de busca em largura
def bfs(adj, n, s):
    # Inicialização
    INF = -1
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    d = [0] * n  # Lista de distâncias
    cor = [0] * n  # Lista de cores para marcar os vértices
    for v in range(n):
        d[v] = INF  # Todas as distâncias começam como -1 (infinito)
        cor[v] = BRANCO  # Todos os vértices começam como não visitados (BRANCO)
    
    d[s] = 0  # Distância do vértice inicial é 0
    cor[s] = CINZA  # Marca o vértice inicial como em processamento
    Q = []
    insere(Q, s)
    
    # Busca em largura
    while not vazio(Q):
        u = remove(Q)
        for v in adj[u]:
            if cor[v] == BRANCO:  # Se o vértice ainda não foi visitado
                d[v] = d[u] + 1  # Atualiza a distância
                cor[v] = CINZA  # Marca o vértice como em processamento
                insere(Q, v)
        cor[u] = PRETO  # Marca o vértice como completamente processado
    
    return d

def main():
    # Lê os valores de n (número de vértices) e m (número de arestas)
    n, m = map(int, input().split())
    
    # Cria uma lista de adjacências para o grafo
    adj = [[] for _ in range(n)]
    
    # Lê as m arestas e constrói o grafo
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)  # Grafo direcionado
    
    # Calcula a matriz de distâncias
    distance_matrix = []
    for i in range(n):
        distance_matrix.append(bfs(adj, n, i))
    
    # Imprime a matriz de distâncias
    for i in range(n):
        print(f"{i}: {' '.join(map(str, distance_matrix[i]))}")

if __name__ == "__main__":
    main()
