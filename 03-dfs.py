# Descricao
# Faça um programa que faz a leitura de um grafo e imprime os instantes de descoberta e de finialização para cada vértice do grafo, de acordo com uma visita DFS (ou busca em profundidade).

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos (o vértice inicial sempre será o vértice 0).
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime os instantes (descoberta e finalização) obtidos pela busca DFS.


# Solucao

def dfs_iterativa():    
    # Lê os valores de n (vértices), m (arestas)
    n, m = (int(tmp) for tmp in input().split(" "))

    # Cria uma lista de adjacências vazia para cada vértice
    adj_list = [[] for _ in range(n)]

    # Lê as arestas e as adiciona na lista de adjacências
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
    
    descoberta = [-1] * n  # Armazena o instante de descoberta dos vértices
    finalizacao = [-1] * n  # Armazena o instante de finalização dos vértices
    visitado = [False] * n  # Marca os vértices visitados
    tempo = [0]  # Variável para contar o tempo (lista para passagem por referência)
    
    def dfs(v):
        stack = [(v, 0)]  # Pilha para simular recursão. (vértice, estado)
        while stack:
            vertice, estado = stack.pop()
            if estado == 0:  # Estado 0 significa que é a primeira vez que visitamos o vértice
                if not visitado[vertice]:
                    visitado[vertice] = True
                    tempo[0] += 1
                    descoberta[vertice] = tempo[0]
                    stack.append((vertice, 1))  # Adiciona o vértice de novo para tratar a finalização
                    # Adiciona os vizinhos (em ordem inversa para manter a ordem correta de processamento)
                    for vizinho in reversed(adj_list[vertice]):
                        if not visitado[vizinho]:
                            stack.append((vizinho, 0))
            elif estado == 1:  # Estado 1 significa que estamos finalizando o vértice
                tempo[0] += 1
                finalizacao[vertice] = tempo[0]
    
    # Iniciar DFS a partir do vértice 0
    for v in range(n):
        if not visitado[v]:
            dfs(v)
    
    # Imprimir os instantes de descoberta e finalização
    print(descoberta)
    print(finalizacao)

# Chamada da função para cálculo dos instantes (descoberta e finalizacao) obtidos pela busca DFS
dfs_iterativa()
