def media(lista):
    if len(lista) == 0:
        return 0
    else:
        soma = 0
        for i , num in enumerate(lista):
            soma+= num

    return soma/len(lista)

print(media([1,2,3,4,5]))

"""
Calcula a média dos valores da lista.

Parâmetros:
- lista (list): Lista de números

Retorno:
- float: Média dos valores

Exceção:
- Levanta erro se a lista estiver vazia

Complexidade:
- Tempo: O(n)
"""