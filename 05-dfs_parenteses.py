# Descricao
# Faça um programa que faz a leitura de um grafo e imprime a expressão de parênteses, de acordo com os instantes de descoberta e de finalização para cada vértice do grafo de  uma visita DFS (busca em profundidade).

# Entrada
# Recebe n, m: n é o total de vértices, m o total de arcos (o vértice inicial sempre será o vértice 0).
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saida
# Imprime a expressão de parênteses de acordo com os instantes (descoberta e finalização) obtidos pela busca DFS.


# Solucao
def visitaDFS(adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO):
    # Descoberta do vértice u
    saidaTexto = "(%d " % u
    tempo[0] += 1
    d[u] = tempo[0]
    cor[u] = CINZA
    
    # Visita todos os vizinhos de u
    for v in adj[u]:
        if cor[v] == BRANCO:
            saidaTexto += visitaDFS(adj, v, d, f, cor, tempo, BRANCO, CINZA, PRETO)
    
    # Finaliza o vértice u
    saidaTexto += "%d) " % u
    tempo[0] += 1
    f[u] = tempo[0]
    cor[u] = PRETO
    return saidaTexto

def dfs(adj, n):
    BRANCO, CINZA, PRETO = 1, 2, 3
    cor = [BRANCO] * n  # Inicialmente todos os vértices estão não visitados (BRANCO)
    d = [-1] * n  # Tempo de descoberta
    f = [-1] * n  # Tempo de finalização
    tempo = [0]  # Contador de tempo
    resultado = ""

    # Executa a DFS a partir de cada vértice ainda não visitado
    for u in range(n):
        if cor[u] == BRANCO:
            resultado += visitaDFS(adj, u, d, f, cor, tempo, BRANCO, CINZA, PRETO)
    
    return resultado.strip()  # Remove espaços extras no final

def main():
    # Lê os valores de n (número de vértices) e m (número de arestas)
    n, m = map(int, input().split())

    # Cria a lista de adjacência
    adj = [[] for _ in range(n)]

    # Lê as arestas e constrói o grafo
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)  # Grafo direcionado

    # Chama a função DFS e obtém a expressão de parênteses
    resultado = dfs(adj, n)

    # Imprime o resultado
    print(resultado)

if __name__ == "__main__":
    main()