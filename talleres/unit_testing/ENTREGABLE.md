## Taller: Pruebas Unitarias – Más allá del verde

Objetivo

La finalidad del taller es entender las limitaciones que tienen las pruebas unitarias. Queremos poder desarrollar un criterio para generar pruebas y no solo para obtener el resultado correcto.

Parte 1 – Exploración inicial

1. Instala las dependencias:


pip install -r requirements.txt


2. Ejecuta las pruebas existentes:


pytest


3. Analiza el resultado general y toma nota de cualquier observación.

Parte 2 – Análisis crítico de las pruebas

Responde en un documento: ¿Las pruebas actuales garantizan la corrección total del código?

* ¿Qué aspectos del comportamiento no están siendo validados?
* ¿Qué tipo de errores podrían pasar desapercibidos?

Parte 3 – El lado oscuro de las pruebas

1. Ubica la función calcular_promedio en:


src/estadistica.py


2. Modifícala para que siempre retorne un valor fijo (por ejemplo, 3.14).
3. Vuelve a ejecutar solo los tests que sean relevantes:


pytest tests/test_estadistica.py -v


4. Analiza el resultado.

Responde:

* ¿Las pruebas detectaron errores?
* ¿Por qué siguen pasando?
* ¿Qué debilidad tienen estos tests?

Parte 4 – Mejora de pruebas

Modifica los tests en:


tests/test_estadistica.py


para que:

* Verifiquen no solo tipos de valores correctos
* Detecten malas implementaciones
* Incluyan casos complementarios:
* Listas vacías
* Un único elemento
* Múltiples valores
* Valores de tipo negativo

Parte 5 – Pruebas con mocks

Utiliza el notebook:


notebooks/03_analizador_mejorado.ipynb


y crea pruebas para analizar_texto que:

* Simulen respuesta satisfactoria
* Simulen fallo y éxito posterior (reintento)
* Simulen fallo total (excepción)

No deberás hacer peticiones reales a internet.

Parte 6 – Reflexión sobre cobertura

Utiliza el notebook:


notebooks/02_coverage_mejorado.ipynb


Me dispongo a responder:

* ¿Qué distinción existe entre la cobertura y la calidad de las pruebas?
* ¿Por qué el 100 % de cobertura no es sinónimo de corrección?

Parte 7 – Reflexión final

Responde:

* ¿Qué te han enseñado las limitaciones de las pruebas unitarias?
* ¿Qué implica que “los tests pasen”?
* ¿Cómo evitarías confusiones en un proyecto en la vida real?

Entregable

Tienen que entregar:

1. Tests mejorados corregidos en:
* tests/test_estadistica.py
* tests/test_analizador.py
2. Documento en formato PDF o Markdown que contenga:
* Las respuestas a las preguntas realizadas
* Las explicaciones de las decisiones de testing
3. Documentos opcionales que contengan casos de pruebas adicionales o las mejoras propuestas

Nota muy importante

Se corroborará no sólo si los tests pasan o no, sino también lo siguiente:
* La calidad de las aserciones
* La capacidad de detectar errores reales
* El uso correcto de mocks
* La profundidad del análisis crítico