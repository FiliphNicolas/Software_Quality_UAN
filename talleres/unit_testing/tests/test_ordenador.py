from src.ordenador import ordenar

def test_vacio():
    assert ordenar([]) == []

def test_un_elemento():
    assert ordenar([5]) == [5]

def test_ya_ordenado():
    assert ordenar([1, 2, 3]) == [1, 2, 3]

def test_otro_ordenado():
    assert ordenar([4, 5, 6]) == [4, 5, 6]