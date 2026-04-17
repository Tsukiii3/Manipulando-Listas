def busca_linear(lista, alvo):

    for i , valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

"""
Realiza busca linear em uma lista.

Percorre todos os elementos até encontrar o valor desejado.

Parâmetros:
- lista (list): Lista de elementos
- alvo: Valor a ser buscado

Retorno:
- int: Índice do elemento ou -1 se não encontrado

Complexidade:
- Tempo: O(n)
"""
