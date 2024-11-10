# Descrição
# Faça um programa que faz a leitura de um grafo e imprime na tela as suas listas de adjacências.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as listas de adjacência.

def ler_grafo():
    # Lê os valores de n (vértices), m (arestas) e ignora qualquer valor extra na linha inicial dado Exemplo2 com valor extra na linha 1
    n, m, *_ = map(int, input().split())

    # Cria uma lista de adjacências vazia para cada vértice
    adj_list = [[] for _ in range(n)]

    # Lê as arestas e as adiciona na lista de adjacências
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    return adj_list

def imprimir_lista_adj(adj_list):
    # Imprime as listas de adjacência
    for i in range(len(adj_list)):
        print(f"{i}: {' '.join(map(str, adj_list[i]))}")

# Leitura do grafo
adj_list = ler_grafo()

# Impressão das listas de adjacência
imprimir_lista_adj(adj_list)
