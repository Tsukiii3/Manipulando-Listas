def menor(lista):
    if len(lista) == 0:
        return 0
    else:
        menor = lista[0]
        indice = 0

        for i , num in enumerate(lista):
            if num < menor:
                menor = num
                indice = i
        return menor, indice

print(menor([1,2,3,4,5]))

"""
Encontra o menor valor da lista e seu índice.

Parâmetros:
- lista (list): Lista de números

Retorno:
- tuple: (menor valor, índice)

Exceção:
- Levanta erro se a lista estiver vazia

Complexidade:
- Tempo: O(n)
"""