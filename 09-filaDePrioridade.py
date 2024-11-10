# Descrição
# Faça um programa que implemente uma fila de prioridade e imprima na tela os resultados das operações especificadas na entrada.

# Entrada
# Na primeira linha, o programa recebe dois inteiros n e k: n é o tamanho da fila, k é a quantidade de operações.
# Inicialmente, a fila Q está vazia, ou seja, Q = [0] * n.
# Na segunda linha, temos n chaves.
# A partir da terceira linha, temos k operações, uma operação por linha.
# Cada operação pode ser:
# - vazio (Q): devolve True se fila vazia, False caso contrário.
# - insere (Q, i): insere o índice i na fila Q, ou seja, faz Q[i] = 1.
# - busca (Q, i): devolve 1 se o índice i estiver na fila, 0 caso contrário (ou seja, devolve Q[i]).
# - extraiMinimo (Q): remove e devolve o índice de Q com a menor chave.
# - minimo (Q): devolve o índice de Q com a menor chave (sem remover).
 
# Saída
# Imprime os resultados das operações com a fila de prioridade.
# Após cada operação "insere", imprima a fila resultante.
# Após "extraiMinimo", imprima o elemento removido e a fila resultante. 
# Após "minimo", imprima o elemento devolvido e a fila resultante.
# Após "busca" ou "vazio", imprima o resultado e a fila.

import numpy as np

# Função para verificar se a fila está vazia
def vazio(Q):
    for i in range(len(Q)):
        if Q[i] == 1:
            return False
    return True

# Função para inserir um índice na fila
def insere(Q, i):
    Q[i] = 1

# Função para buscar o índice com a menor chave na fila (sem remover)
def minimo(Q, chave):
    for i in range(len(Q)):
        if Q[i] == 1:
            min_indice = i
            break
    for i in range(len(Q)):
        if Q[i] == 1 and chave[i] < chave[min_indice]:
            min_indice = i
    return min_indice

# Função para extrair (remover) o índice com a menor chave na fila
def extraiMinimo(Q, chave):
    min_indice = minimo(Q, chave)
    Q[min_indice] = 0
    return min_indice

# Função para buscar um índice específico na fila
def busca(Q, v):
    return Q[v]

# Função principal para processar a fila de prioridade
def filaPrioridade():
    # Leitura dos dados de entrada
    n, k = (int(x) for x in input().split(" "))
    chaves = np.array([int(x) for x in input().split(" ")])

    # Inicializa a fila vazia
    Q = [0] * n

    # Processamento das operações
    for _ in range(k):
        operacao = input()
        
        # Determina o tipo de operação e executa-a
        if len(operacao) > 1:
            operacao, j = operacao.split(" ")
            j = int(j)
        
        if operacao == "I":
            insere(Q, j)
            print(Q)
        elif operacao == "M":
            min_indice = minimo(Q, chaves)
            print(min_indice, chaves[min_indice], Q)
        elif operacao == "E":
            min_indice = extraiMinimo(Q, chaves)
            print(min_indice, chaves[min_indice], Q)
        elif operacao == "V":
            print(vazio(Q), Q)
        elif operacao == "B":
            print(busca(Q, j), Q)

# Chama a função principal
filaPrioridade()
