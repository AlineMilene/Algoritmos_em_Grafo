# Descrição
# Faça um programa que faz a leitura de um grafo ponderado e imprime na tela as suas listas de adjacências com os pesos de cada arco.

# Entrada
# Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída
# Imprime as listas de adjacência com os pesos.

def grafoPonderado():
    # Leitura dos dados de entrada
    n, m = (int(x) for x in input().split(" "))
    
    # Inicializa o grafo como um dicionário de listas
    grafo = {i: [] for i in range(n)}
    
    # Lê cada arco e adiciona à lista de adjacência do grafo
    for _ in range(m):
        u, v, peso = (int(x) for x in input().split(" "))
        grafo[u].append((v, peso))
    
    # Imprime as listas de adjacência com pesos
    for i in range(n):
        saida = f"{i}: "
        for (v, peso) in grafo[i]:
            saida += f"{v}({peso}) "
        print(saida)

# Chama a função
grafoPonderado()
