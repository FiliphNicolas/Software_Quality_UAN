# Conclusiones del Análisis de Tests

## 1. Análisis Crítico de los Tests Existentes


los tests de iniciacion de presentaban varias maneras deblilidades: 

- **test_estadistica.py**: Se verifican tipo de retorno, caso vacío y por falta de irregularidad.  Que No validaba en el cálculo correcto del promedio, lo que permitió que un bug (retornar siempre 3.14) pasara desapercibido.
- **test_analizador.py**: error al ejecutar con la función `ordenar` en vez  `analizar_texto`. solamente un placeholder.
- **test_ordenador.py**: Solamente un placeholder, sin tests eficiente.

## 2. Debilidades Identificadas

- Falta de verificación de valores correctos en los cálculos.
- Tests no exhaustivos (solo casos básicos).
- Archivos de tests mal asignados.
- No Existen test ni ensayos para las funciones que llaman externas (analizar_texto).
- No se probaban casos edge como un ejemplo números negativos, floats, etc.

## 3. Modificación de calcular_promedio y Detección por Tests

Se modificó la función `calcular_promedio` para que siempre devuelva el número 3.14. Como el resto de tests no comprueba el valor que se devuelve, no detectaron el bug. Después se añade un nuevo test en el que se comprueban valores correctos y, por consiguiente los tests fallan, como es de esperar, detectando error.

## 4. Correcciones en test_estadistica.py

Se agregaron tests para:
- Promedio correcto con enteros.
- Promedio con un elemento.
- Promedio con floats.

## 5. Implementación de Pruebas con Mocks en analizar_texto

Se implementaron tests usando `unittest.mock` para simular `requests.get`:
- Fue aceptado.
- Fallo después de reintentos.
- Éxito en segundo intento.

Esto evita llamadas externas y hace los tests determinísticos.

## 6. Revisión de Cobertura de Código

Cobertura del 100% en todos los módulos:
- src/__init__.py: 100%
- src/analizador.py: 100%
- src/estadistica.py: 100%
- src/ordenador.py: 100%

## Conclusiones Generales

Los tests, mejorados en la actualidad, son ahora más robustos, más exhaustivos, cubren los casos edge, utilizan mocks para el aislamiento, y logran una perfecta cobertura. Las debilidades iniciales nos hicieran ver la necesidad de tests exhaustivos que no sólo verifiquen tipos y errores, sino también valores y comportamientos esperados.</content>
<parameter name="filePath">c:\Users\nico\Desktop\Software_Quality_UAN\talleres\unit_testing\respuestas.md