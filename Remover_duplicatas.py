def remover_duplicados(lista):
    semDuplicados = []

    for num in lista:
        if num not in semDuplicados:
            semDuplicados.append(num)
    return semDuplicados

print(remover_duplicados([1,1,2,2,2,3,4,5,5]))

"""
Remove elementos duplicados da lista mantendo a ordem.

Parâmetros:
- lista (list): Lista de elementos

Retorno:
- list: Lista sem duplicados

Complexidade:
- Tempo: O(n²)
"""


