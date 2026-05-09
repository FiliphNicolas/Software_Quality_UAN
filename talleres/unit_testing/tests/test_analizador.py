import pytest
from unittest.mock import patch, Mock
from src.analizador import analizar_texto
import requests

@patch('src.analizador.requests.get')
def test_analizar_texto_exitoso(mock_get):
    mock_response = Mock()
    mock_response.text = "Hola\nMundo\n"
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    lineas, caracteres = analizar_texto("http://example.com")
    assert lineas == 3
    assert caracteres == 9  # Hola(4) + Mundo(5) + ''(0) = 9

@patch('src.analizador.requests.get')
def test_analizar_texto_falla_despues_reintentos(mock_get):
    mock_get.side_effect = requests.RequestException("Error de conexión")

    with pytest.raises(RuntimeError, match="No se pudo acceder a la URL después de 3 intentos"):
        analizar_texto("http://example.com")

@patch('src.analizador.requests.get')
def test_analizar_texto_exito_en_segundo_intento(mock_get):
    mock_response = Mock()
    mock_response.text = "Texto"
    mock_response.raise_for_status.return_value = None

    mock_get.side_effect = [requests.RequestException("Primero falla"), mock_response]

    lineas, caracteres = analizar_texto("http://example.com")
    assert lineas == 1
    assert caracteres == 5