def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) -1

    while inicio <= fim:
        meio = (fim+inicio)//2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

print(busca_binaria([1,2,3,4,5,6,7,8,9], 3))


"""
Realiza busca binária em uma lista ordenada.

A cada iteração, reduz o espaço de busca pela metade,
tornando o algoritmo eficiente para grandes volumes de dados.

Parâmetros:
- lista (list): Lista ordenada de elementos
- alvo: Valor a ser buscado

Retorno:
- int: Índice do elemento ou -1 se não encontrado

Complexidade:
- Tempo: O(log n)

Observação:
- A lista deve estar ordenada
"""

