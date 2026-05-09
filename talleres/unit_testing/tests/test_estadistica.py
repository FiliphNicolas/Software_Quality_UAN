import pytest
from src.estadistica import calcular_promedio

def test_tipo_retorno_float():
    res = calcular_promedio([1, 2, 3])
    assert isinstance(res, float)

def test_lista_vacia_retorna_none():
    assert calcular_promedio([]) is None

def test_no_lanza_excepcion():
    try:
        calcular_promedio([5])
    except Exception:
        pytest.fail("No debería lanzar excepción")

def test_promedio_correcto():
    assert calcular_promedio([1, 2, 3, 4]) == 2.5

def test_promedio_un_elemento():
    assert calcular_promedio([10]) == 10.0

def test_promedio_con_floats():
    assert calcular_promedio([1.5, 2.5]) == 2.0