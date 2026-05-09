import pytest
from src.estadistica import calcular_promedio

def test_tipo_retorno_float():
    """Verifica que el retorno sea float y que el valor sea correcto"""
    res = calcular_promedio([1, 2, 3])
    assert isinstance(res, float)
    assert res == 2.0  # También verificamos que el valor sea correcto

def test_lista_vacia_retorna_none():
    """Verifica que lista vacía retorne None"""
    assert calcular_promedio([]) is None

def test_no_lanza_excepcion_con_entrada_valida():
    """Verifica que no lanza excepción con entrada válida"""
    try:
        calcular_promedio([5])
    except Exception:
        pytest.fail("No debería lanzar excepción con entrada válida")

def test_promedio_correcto():
    """Verifica promedio con múltiples valores"""
    assert calcular_promedio([1, 2, 3, 4]) == 2.5

def test_promedio_un_elemento():
    """Verifica promedio con un solo elemento"""
    assert calcular_promedio([10]) == 10.0

def test_promedio_con_floats():
    """Verifica promedio con valores flotantes"""
    assert calcular_promedio([1.5, 2.5]) == 2.0

# Tests mejorados adicionales

def test_promedio_valores_negativos():
    """Verifica promedio con valores negativos"""
    assert calcular_promedio([-1, -2, -3]) == -2.0
    assert calcular_promedio([-1, 1]) == 0.0

def test_promedio_con_ceros():
    """Verifica promedio con ceros"""
    assert calcular_promedio([0, 0, 0]) == 0.0
    assert calcular_promedio([0, 5, 10]) == 5.0

def test_promedio_valores_mixtos():
    """Verifica promedio con valores positivos y negativos"""
    assert calcular_promedio([-2, 0, 2]) == 0.0
    assert calcular_promedio([-5, 5, 10]) == 3.3333333333333335

def test_promedio_precision_decimal():
    """Verifica precisión con operaciones complejas"""
    result = calcular_promedio([1.1, 2.2, 3.3])
    assert abs(result - 2.2) < 1e-10  # Permitir pequeña diferencia por punto flotante

def test_promedio_valores_grandes():
    """Verifica con valores grandes"""
    assert calcular_promedio([1000000, 2000000, 3000000]) == 2000000.0

def test_promedio_valores_pequenos():
    """Verifica con valores muy pequeños"""
    result = calcular_promedio([0.001, 0.002, 0.003])
    assert abs(result - 0.002) < 1e-10

def test_lanza_excepcion_con_tipos_invalidos():
    """Verifica que lanza excepción con tipos de datos incorrectos"""
    with pytest.raises(TypeError):
        calcular_promedio([1, "dos", 3])
    
    with pytest.raises(TypeError):
        calcular_promedio(["a", "b", "c"])
    
    with pytest.raises(TypeError):
        calcular_promedio([True, False, True])

def test_no_modifica_lista_original():
    """Verifica que no modifica la lista original"""
    original = [1, 2, 3]
    calcular_promedio(original)
    assert original == [1, 2, 3]  # La lista debe permanecer intacta

def test_promedio_con_valores_extremos():
    """Verifica con valores extremos"""
    # Con valores muy grandes
    result = calcular_promedio([1e10, -1e10, 0])
    assert result == 0.0
    
    # Con valores muy pequeños
    result = calcular_promedio([1e-10, 2e-10, 3e-10])
    assert abs(result - 2e-10) < 1e-15