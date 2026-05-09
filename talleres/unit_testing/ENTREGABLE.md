# Taller: Pruebas Unitarias – Más allá del verde

## Objetivo

El objetivo de este taller es conocer las limitaciones de las pruebas unitarias y desarrollar criterio para generar pruebas adecuadas, y no únicamente para obtener resultados "en verde".

---

## Parte 1 – Exploración inicial

1. Instala las dependencias:

```
pip install -r requirements.txt
```

2. Ejecuta las pruebas existentes:

```
pytest
```

3. Observa el resultado de general.

---

## Parte 2 – Análisis crítico de las pruebas

Responde en un documento:

* ¿Las pruebas actuales garantizan que el código es correcto?
* ¿Qué aspectos del comportamiento NO están siendo validados?
* ¿Qué tipo de errores podrían pasar desapercibidos?

---

## Parte 3 – El lado oscuro de las pruebas

1. Ubica la función `calcular_promedio` en:

```
src/estadistica.py
```

2. Modifícala para que SIEMPRE retorne un valor fijo (por ejemplo `3.14`).

3. Vuelve a ejecutar SOLO los tests que sean relevantes:
```
pytest tests/test_estadistica.py -v
```

4. Analiza el resultado.

Responde:

* ¿Las pruebas detectaron presentaron error?
* ¿Por qué siguen pasando?
* ¿Qué debilidad tienen estos tests?

---

## Parte 4 – Mejora de pruebas

Modifica los tests en:

```
tests/test_estadistica.py
```

para que:

* Verifiquen no solo tipos de valores correctos
* Detecten malas implementaciones
* Incluyan casos complementarios:

  * listas vacías
  * un único elemento
  * múltiples valores
  * valores de tipo negativo

---

## Parte 5 – Pruebas con mocks

Utiliza el notebook:

```
notebooks/03_analizador_mejorado.ipynb
```

y crea pruebas para `analizar_texto` que:

* Simulen respuesta satisfactoria
* Simulen fallo y éxito posterior (reintento)
* Simulen fallo total (excepción)

No deberás hacer peticiones reales a internet.

---

## Parte 6 – Reflexión sobre cobertura

Utiliza el notebook:

```
notebooks/02_coverage_mejorado.ipynb
```

Me dispongo a responder:
* ¿Qué distinción existe entre cobertura y la calidad de las pruebas?
* ¿Por qué el 100 % de cobertura no es sinónimo de corrección?

---

## 🧠 Parte 7 – Reflexión final

Responde:

* ¿Qué te han enseñado las limitaciones de las pruebas unitarias?
* ¿Qué implica que “los tests pasen”?
* ¿Cómo evitarías confusiones erróneas en un proyecto en la vida real?

---

## 📦 Entregable

Tienen que entregar:

1. Tests mejorados corregido en:

   * `tests/test_estadistica.py`
   * `tests/test_analizador.py`

2. Documento (PDF o Markdown) con:

   * Respuestas a las preguntas
   * Explicaciones de decisiones de testing

3. (Opcional) Casos adicionales o mejoras propuestas

---

## ⚠️ Nota importante

No solo se revisará si los tests pasan, sino:

* La calidad de las aserciones
* La capacidad de detectar errores reales
* El uso correcto de mocks
* La profundidad del análisis crítico

---
