# Descrição
# Faça um programa que implemente as operações com Conjuntos Disjuntos e imprima os resultados correspondentes.

# Entrada
# Inicialmente, S é vazio.
# A primeira linha contém n, o total de operações com S.
# As linhas a seguir, temos n linhas, cada uma com uma operação:
# - findSet (S, x): devolve um representante de S_x.
# - makeSet (S, x): cria um novo conjunto com um único elemento x.
# - union (S, x, y): une dois conjuntos S_x e S_y.

# Saída
# Imprime os resultados das operações com Conjuntos Disjuntos.
# Após cada operação "makeSet" ou "union", imprima o S resultante.
# Após cada operação "findSet" imprima o índice (representante) e S.

def findSet(S, x):
    for i in range(len(S)):
        for j in S[i]:
            if j == x:
                return i
    return -1  # Retorna -1 caso o elemento não seja encontrado

def makeSet(S, x):
    S.append([x])

def union(S, x, y):
    i = findSet(S, x)
    j = findSet(S, y)
    if i != -1 and j != -1 and i != j:
        S[i] += S[j]
        S[j].clear()

def main():
    # Lê o número de operações
    n = int(input())
    # Inicialmente, S é vazio
    S = []

    # Lê e executa as operações
    for _ in range(n):
        tmp = input().split()
        op = tmp[0]
        arg1 = tmp[1]
        
        if op == "M":  # makeSet
            makeSet(S, arg1)
            print(S)
        elif op == "F":  # findSet
            representative = findSet(S, arg1)
            print(representative, S)
        elif op == "U":  # union
            arg2 = tmp[2]
            union(S, arg1, arg2)
            print(S)

# Executa o programa
if __name__ == "__main__":
    main()
