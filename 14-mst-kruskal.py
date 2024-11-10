# Descrição
# Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Kruskal.

# Entrada
# Recebe n, m; n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)
 
# Saída
# Imprime a lista das arestas na ordem de inserção pelo algoritmo de Kruskal (i, j, peso).

def findSet(S, x):
    for i in range(len(S)):
        if x in S[i]:
            return i
    return -1


def makeSet(S, x):
    S.append({x})


def union(S, x, y):
    i = findSet(S, x)
    j = findSet(S, y)
    if i != -1 and j != -1 and i != j:
        S[i] = S[i].union(S[j])
        S.pop(j)


def kruskal(n, edges):
    # Inicializa a árvore geradora mínima (T) e o conjunto disjunto (S)
    T = []   # Árvore geradora mínima resultante
    S = []
    for i in range(n):
        makeSet(S, i)

    # Ordena as arestas pelo peso (menor para maior)
    edges.sort(key=lambda edge: edge[2])

    # Adiciona arestas à MST usando o algoritmo de Kruskal
    for u, v, peso in edges:
        if findSet(S, u) != findSet(S, v):
            union(S, u, v)
            T.append([u, v, peso])

    return T


def main():
    # Leitura do número de vértices e arestas
    data = input().split()
    n = int(data[0])  # número de vértices
    m = int(data[1])  # número de arestas

    # Ignora qualquer valor extra (ex: o terceiro número no exemplo 2)
    edges = []
    for _ in range(m):
        u, v, peso = map(int, input().split())
        edges.append([u, v, peso])

    # Executa o algoritmo de Kruskal e obtém a MST
    mst = kruskal(n, edges)

    # Exibe a MST
    print(mst)

# Executa o programa
if __name__ == "__main__":
    main()