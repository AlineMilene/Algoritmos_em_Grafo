# Descricao
# Faça um programa que faz a leitura de um grafo e imprime na tela as listas de adjacências do seu grafo transposto.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime as listas de adjacência do grafo transposto.


# Solucao
def grafo_transposto(n, m, arestas):
    # Cria uma lista de adjacências para o grafo transposto
    adjTransposto = [[] for _ in range(n)]

    # Lê as arestas do grafo original e constrói o grafo transposto
    for i, j in arestas:
        adjTransposto[j].append(i)  # No grafo transposto, a aresta é invertida

    return adjTransposto

def imprime_grafo_transposto(adjTransposto):
    # Imprime as listas de adjacência do grafo transposto
    for j in range(len(adjTransposto)):
        saida = "%d: " % j
        saida += " ".join(map(str, adjTransposto[j]))
        print(saida)

def main():
    # Lê os dados de entrada
    n, m = map(int, input().split())
    arestas = [tuple(map(int, input().split())) for _ in range(m)]

    # Obtém o grafo transposto
    adjTransposto = grafo_transposto(n, m, arestas)

    # Imprime o grafo transposto
    imprime_grafo_transposto(adjTransposto)

if __name__ == "__main__":
    main()