# Parte 3 - El Lado Oscuro de las Pruebas

## Experimento: Modificación maliciosa de calcular_promedio

### Cambio realizado:
```python
# Original:
def calcular_promedio(numeros):
    if not numeros:
        return None
    return sum(numeros) / len(numeros)

# Modificado:
def calcular_promedio(numeros):
    if not numeros:
        return None
    return 3.14
```

### Resultados de los tests:

**Tests que PASARON (3/6):**
- ✅ `test_tipo_retorno_float` - Solo verificó que fuera float, no el valor correcto
- ✅ `test_lista_vacia_retorna_none` - El caso de lista vacía sigue funcionando
- ✅ `test_no_lanza_excepcion` - No hay excepciones, todo "funciona"

**Tests que FALLARON (3/6):**
- ❌ `test_promedio_correcto` - Esperaba 2.5 pero obtuvo 3.14
- ❌ `test_promedio_un_elemento` - Esperaba 10.0 pero obtuvo 3.14
- ❌ `test_promedio_con_floats` - Esperaba 2.0 pero obtuvo 3.14

## Análisis de las preguntas:

### ¿Las pruebas detectaron errores?
**Parcialmente.** Solo 3 de 6 tests detectaron que algo estaba mal. Esto es preocupante porque el 50% de los tests pasaron con una implementación completamente incorrecta.

### ¿Por qué siguen pasando algunos tests?
Porque estos tests son demasiado débiles:
1. **`test_tipo_retorno_float`**: Solo verifica el tipo, no el valor. Cualquier float pasaría.
2. **`test_lista_vacia_retorna_none`**: Solo prueba el caso edge, no el comportamiento normal.
3. **`test_no_lanza_excepcion`**: Solo verifica que no haya crashes, no que el resultado sea correcto.

### ¿Qué debilidad tienen estos tests?
1. **Aserciones demasiado específicas**: Algunos tests solo verifican una cosa (tipo, excepción, caso edge)
2. **Falta de validación de valores correctos**: No todos los tests verifican que el cálculo sea correcto
3. **Tests aislados**: No hay tests que verifiquen múltiples aspectos simultáneamente
4. **Falsa confianza**: El hecho de que 3 tests pasan da una falsa sensación de que todo está bien

## Lección aprendida:

**"Los tests pasan" no significa que el código sea correcto.** Una implementación completamente errónea puede hacer que la mitad de los tests pasen si los tests son demasiado débiles.

Esto demuestra por qué es crucial:
- Escribir tests que verifiquen el comportamiento real, no solo propiedades superficiales
- Incluir múltiples casos de prueba para cada función
- Verificar tanto los casos normales como los casos edge
- No confiar únicamente en que "los tests pasan" como medida de calidad
