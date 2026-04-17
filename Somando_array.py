def soma (lista):
    if len(lista) == 0:
        return 0
    else:
        soma = 0
        for i, num in enumerate(lista):
            soma += num
    return soma

print(soma([1,2,3,4,5]))

#Versão recursiva
def soma_recursao(lista):
    if len(lista) == 0:
        return 0
    else:
       return lista[0] + soma_recursao(lista[1:])

print(soma([1,2,3,4,5]))

"""
Calcula a soma de todos os elementos da lista.

Parâmetros:
- lista (list): Lista de números

Retorno:
- int/float: Soma dos valores

Complexidade:
- Tempo: O(n)
"""

"""
Calcula a soma dos elementos da lista utilizando recursão.

Parâmetros:
- lista (list): Lista de números

Retorno:
- int/float: Soma dos valores

Complexidade:
- Tempo: O(n)
"""