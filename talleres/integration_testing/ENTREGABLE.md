## Taller: Integration Testing

🎯 Objetivo

El propósito de este taller es desarrollar criterio técnico para diseñar pruebas de integración efectivas, capaces de validar correctamente la interacción entre módulos y detectar:

- Fallos de comunicación entre componentes
- Estados inconsistentes
- Dependencias no controladas
- Integraciones incompletas o mal aisladas

Durante la actividad se aplicarán los enfoques clásicos de pruebas de integración:

- Top-Down
- Bottom-Up
- Sandwich
- Big-Bang

Además, se utilizarán técnicas de apoyo como stubs y drivers.

━━━━━━━━━━━━━━━━━━
📌 Modalidad de trabajo
━━━━━━━━━━━━━━━━━━

El taller puede desarrollarse:

- De forma individual
- En grupos de máximo 3 integrantes

━━━━━━━━━━━━━━━━━━
⚙️ Preparación del entorno
━━━━━━━━━━━━━━━━━━

Crear el entorno virtual e instalar dependencias

Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Linux / macOS:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Ejecutar las pruebas iniciales:
```bash
pytest tests/ -v
```

━━━━━━━━━━━━━━━━━━
☑️ Actividades
━━━━━━━━━━━━━━━━━━

🔍 Análisis inicial

Analicen críticamente las pruebas de integración existentes.

- Identifiquen qué interacciones entre módulos no están siendo verificadas.
- Determinen posibles falsos positivos o escenarios no cubiertos.

━━━━━━━━━━━━━━━━━━
🧨 Sabotaje controlado
━━━━━━━━━━━━━━━━━━

Modifiquen el método add_task en service.py para que:

- Retorne siempre True
- No utilice storage
- No invoque notifier

Luego:

- Ejecuten nuevamente las pruebas
- Verifiquen si los tests actuales detectan el problema
- Reflexionen sobre las limitaciones de las pruebas existentes

━━━━━━━━━━━━━━━━━━
🧩 Aplicación de enfoques de integración
━━━━━━━━━━━━━━━━━━

🔼 Top-Down Testing

- Creen stubs para Storage y Notifier
- Prueben la lógica del módulo Service
- Validen el comportamiento esperado ante distintos escenarios

🔽 Bottom-Up Testing

- Implementen un driver
- Prueben el módulo Storage de forma aislada
- Evalúen entradas válidas e inválidas

🔀 Sandwich Testing

- Combinen módulos reales con stubs
- Diseñen pruebas híbridas que validen integraciones parciales

━━━━━━━━━━━━━━━━━━
🧪 Mejora de cobertura de integración
━━━━━━━━━━━━━━━━━━

Extiendan las pruebas para cubrir al menos los siguientes casos:

- Fallo durante el almacenamiento
- Fallo durante la notificación
- Títulos vacíos
- Tareas duplicadas
- Consistencia del sistema ante errores parciales

━━━━━━━━━━━━━━━━━━
🧠 Reflexión técnica
━━━━━━━━━━━━━━━━━━

Expliquen la diferencia entre:

- Cobertura de código
- Cobertura de integración

Incluyan ejemplos observados durante el taller.

━━━━━━━━━━━━━━━━━━
📘 Material de apoyo
━━━━━━━━━━━━━━━━━━

En la carpeta notebooks/ encontrarán notebooks con:

- Explicaciones sobre stubs y drivers
- Ejemplos de cada estrategia de integración
- Casos de sabotaje controlado
- Buenas prácticas para diseño de pruebas

━━━━━━━━━━━━━━━━━━
🏁 Entrega
━━━━━━━━━━━━━━━━━━

La entrega se realiza mediante un Pull Request (PR) hacia la rama principal (main), creado desde una rama cuyo nombre identifique al estudiante o al equipo.

📌 Entrega individual

Usar el formato: `nombre_apellido1_apellido2`

Ejemplo: `juan_perez_gomez`

📌 Entrega grupal (máximo 3 personas)

Usar los apellidos de todos los integrantes unidos por guiones bajos, en el orden que prefieran.

Ejemplo: `perez_gomez_lopez`

También pueden anteponer la palabra grupo si lo desean: `grupo_perez_gomez_lopez`

En la descripción del Pull Request deben aparecer:

- Nombres completos de todos los integrantes
- Código estudiantil o identificación de cada integrante

━━━━━━━━━━━━━━━━━━
📋 Criterios de evaluación
━━━━━━━━━━━━━━━━━━

Se evaluará:

- Calidad de las aserciones de integración
- Capacidad de detectar fallos de comunicación entre componentes
- Uso correcto de stubs y drivers
- Profundidad del análisis crítico
- Aplicación correcta de los enfoques Top-Down, Bottom-Up y Sandwich
- Documentación de reflexiones técnicas
