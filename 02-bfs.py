# Descricao
# Faça um programa que faz a leitura de um grafo e imprime as distâncias obtidas a partir de um vértice s, de acordo com uma visita BFS (ou busca em largura).

# Entrada
# Recebe n, m e s: n é o total de vértices, m o total de arcos e s o vértice inicial.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime as distâncias obtidas a partir de s, pela busca BFS.


# Solucao

def bfs_distance(n, m, s):
    # Criação da lista de adjacência
    adj = [[] for _ in range(n)]

    # Leitura das arestas
    for _ in range(m):
        i, j = (int(tmp) for tmp in input().split())
        adj[i].append(j)
    
    # Inicialização
    d = [float('inf')] * n  # Distâncias iniciais como infinito
    cor = [0] * n  # Cores dos vértices
    d[s] = 0  # Distância do vértice inicial é 0
    cor[s] = 1  # Marca o vértice inicial como visitado

    # Fila para BFS
    Q = [s]

    while Q:  # Enquanto a fila não estiver vazia
        u = Q.pop(0)  # Remove o primeiro elemento da fila
        for v in adj[u]:  # Para cada vértice adjacente
            if cor[v] == 0:  # Se o vértice ainda não foi visitado (BRANCO)
                d[v] = d[u] + 1  # Atualiza a distância
                cor[v] = 1  # Marca como visitado (CINZA)
                Q.append(v)  # Adiciona o vértice à fila
        cor[u] = 2  # Marca o vértice como totalmente visitado (PRETO)

    # Impressão das distâncias
    print(f"{s}: " + " ".join(map(str, d)))
    
# Lê os valores de n (vértices), m (arestas) e o vértice inicial s
n, m, s = (int(tmp) for tmp in input().split(" "))

# Chamada da função para cálculo das distâncias à partir de um vértice s em um grafo utilizando BFS
bfs_distance(n, m, s)