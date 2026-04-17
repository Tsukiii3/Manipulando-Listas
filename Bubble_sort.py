def bubble_sort(lista):
    lista_ordenada = lista.copy()
    n = len(lista_ordenada)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada

"""
Ordena uma lista utilizando o algoritmo Bubble Sort.

Compara elementos adjacentes e os troca de posição
caso estejam fora de ordem.

Parâmetros:
- lista (list): Lista de números

Retorno:
- list: Nova lista ordenada

Complexidade:
- Tempo: O(n²)
"""