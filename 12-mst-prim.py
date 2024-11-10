# Descrição
# Faça um programa que leia um grafo ponderado e calcule uma árvore geradora mínima pelo algoritmo de Prim.

# Entrada
# Recebe n, m e r; n é o total de vértices, m o total de arcos e r é a raiz da árvore geradora mínima.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime dois vetores.
# Na primeira linha, o vetor das "chaves".
# Na segunda linha, o vetor de "pai" (para representar a árvore).

# Função para verificar se a fila Q está vazia
def vazio(Q):
    for i in range(len(Q)):
        if Q[i] == 1:
            return False
    return True

# Função para inserir um elemento na fila Q
def insere(Q, i):
    Q[i] = 1

# Função para encontrar o índice do elemento com o valor mínimo na chave
# Assumindo que Q não está vazia
def minimo(Q, chave):
    for i in range(len(Q)):
        if Q[i] == 1:
            min = i
            break
    for i in range(len(Q)):
        if Q[i] == 1 and chave[i] < chave[min]:
            min = i
    return min   # Devolve índice de um vértice

# Função para extrair o índice do elemento com o valor mínimo na chave
# Assumindo que Q não está vazia
def extraiMinimo(Q, chave):
    for i in range(len(Q)):
        if Q[i] == 1:
            min = i
            break
    for i in range(len(Q)):
        if Q[i] == 1 and chave[i] < chave[min]:
            min = i
    Q[min] = 0
    return min   # Devolve índice de um vértice

# Função para verificar se um vértice está na fila Q
def busca(Q, v):
    return Q[v]

# Função principal que executa o algoritmo de Prim
def prim(n, m, r, arestas):
    # Inicializar a matriz de adjacência com 0
    matrizAdj = [[0 for _ in range(n)] for _ in range(n)]
    
    # Preencher a matriz de adjacência com os pesos das arestas
    for i, j, peso in arestas:
        matrizAdj[i][j] = peso

    # Inicializar variáveis
    INF = float('inf')
    NIL = -1
    chave = [INF] * n
    pai = [NIL] * n
    chave[r] = 0
    Q = [1] * n  # Todos os vértices estão na fila de prioridade

    # Loop principal do algoritmo de Prim
    while not vazio(Q):
        u = extraiMinimo(Q, chave)
        for v in range(n):
            weight = matrizAdj[u][v]
            if weight > 0:  # Verifica se existe uma aresta entre u e v
                if busca(Q, v) and weight < chave[v]:
                    chave[v] = weight
                    pai[v] = u

    return chave, pai

# Função de entrada e saída
def main():
    # Leitura dos dados de entrada
    n, m, r = map(int, input("Digite o número de vértices, arestas e a raiz: ").split())
    arestas = []
    for _ in range(m):
        i, j, peso = map(int, input().split())
        arestas.append((i, j, peso))

    # Executar o algoritmo de Prim
    chave, pai = prim(n, m, r, arestas)

    # Exibir o resultado
    print(chave)
    print(pai)

# Chamada da função principal
if __name__ == "__main__":
    main()
