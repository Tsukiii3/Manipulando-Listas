def maior (lista):
    if len(lista) == 0:
        return 0
    else:
        maior = lista[0]
        indice = 0

        for i, num in enumerate(lista):
            if num > maior:
                maior = num
                indice = i

        return maior, indice

print(maior([1,2,3,4,5]))

"""
Encontra o maior valor da lista e seu índice.

Parâmetros:
- lista (list): Lista de números

Retorno:
- tuple: (maior valor, índice)

Exceção:
- Levanta erro se a lista estiver vazia

Complexidade:
- Tempo: O(n)
"""