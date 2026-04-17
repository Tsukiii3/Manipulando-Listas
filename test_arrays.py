from Manipulando_Listas.Bubble_sort import bubble_sort
from Manipulando_Listas.Busca_binária import busca_binaria
from Manipulando_Listas.Busca_Linear import busca_linear
from Manipulando_Listas.maior_numero_da_lista import maior
from Manipulando_Listas.menor_numero_da_lista import menor
from Manipulando_Listas.Média_array import media
from Manipulando_Listas.Remover_duplicatas import remover_duplicados
from Manipulando_Listas.Somando_array import soma, soma_recursao


def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]


def test_busca_binaria():
    lista = [1, 2, 3, 4, 5]
    assert busca_binaria(lista, 3) == 2
    assert busca_binaria(lista, 10) == -1


def test_busca_linear():
    lista = [5, 3, 8]
    assert busca_linear(lista, 3) == 1
    assert busca_linear(lista, 10) == -1


def test_maior():
    assert maior([1, 5, 3]) == (5, 1)


def test_menor():
    assert menor([1, 5, 3]) == (1, 0)


def test_media():
    assert media([2, 4, 6]) == 4


def test_remover_duplicados():
    assert remover_duplicados([1, 1, 2, 2, 3]) == [1, 2, 3]


def test_soma():
    assert soma([1, 2, 3]) == 6


def test_soma_recursao():
    assert soma_recursao([1, 2, 3]) == 6