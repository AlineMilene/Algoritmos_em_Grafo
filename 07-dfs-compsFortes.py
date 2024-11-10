# Descricao
# Faça um programa que faz a leitura de um grafo e imprime a expressão de parênteses dos componentes fortemente conexos.

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime a expressão de parênteses dos componentes fortemente conexos.


# Solucao

# Funcao para executar a busca em profundidade (DFS) em um grafo
def visitaDFS(adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO):
    # Marca a descoberta do vértice u
    saidaTexto = "(%d " % u
    tempo[0] += 1
    d[u] = tempo[0]
    cor[u] = CINZA
    
    # Explora os vizinhos de u
    for v in adj[u]:
        if cor[v] == BRANCO:
            saidaTexto += visitaDFS(adj, v, d, f, cor, tempo, BRANCO, CINZA, PRETO)
    
    # Finaliza a visita ao vértice u
    saidaTexto += "%d) " % u
    tempo[0] += 1
    f[u] = tempo[0]
    cor[u] = PRETO
    
    return saidaTexto

# Função para realizar DFS em todo o grafo
def dfs(adj, verticesOrdenados, n):
    # Inicializa as constantes para as cores
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    
    # Inicializa os arrays para cores, tempo de descoberta e finalização
    cor = [BRANCO] * n
    d = [0] * n
    f = [0] * n
    
    tempo = [0]
    saidaTexto = ""
    
    # Executa DFS para cada vértice na ordem dada
    for u in verticesOrdenados:
        if cor[u] == BRANCO:
            saidaTexto += visitaDFS(adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO)
    
    return d, f, saidaTexto

# Função para criar a lista de adjacências transposta
def criaListaAdjacenciasTransposta(matrizAdj, n):
    adjT = [[] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            if matrizAdj[i][j] > 0:
                adjT[j].append(i)
    return adjT

# Função principal para ler dados e executar o algoritmo
def main():
    n, m = (int(tmp) for tmp in input().split(" "))

    # Cria matriz de adjacência e lista de adjacências
    matrizAdj = [[0 for _ in range(n)] for _ in range(n)]
    adj = [[] for _ in range(n)]

    # Leitura dos arcos do grafo
    for _ in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        adj[i].append(j)
        matrizAdj[i][j] = 1

    # Executa o algoritmo DFS no grafo original
    d, f, saidaTexto = dfs(adj, range(n), n)

    # Ordena os vértices pela ordem de finalização em ordem decrescente
    import numpy as np
    verticesOrdenados = np.argsort(f)[::-1]

    # Criação da lista de adjacências transposta
    adjT = criaListaAdjacenciasTransposta(matrizAdj, n)

    # Executa o algoritmo DFS na lista de adjacências transposta
    d, f, saidaTextoTransposta = dfs(adjT, verticesOrdenados, n)

    # Imprime a saída no formato desejado
    print(saidaTexto)

if __name__ == "__main__":
    main()

