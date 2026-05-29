## Taller: Pruebas E2E — Del navegador al sistema completo

🎯 Objetivo

Comprender qué son las pruebas de extremo a extremo (End-to-End), cuándo son necesarias, cómo se implementan con Playwright en Python, y cuáles son sus principales limitaciones y antipatrones. Como complemento, se introduce Selenium para comprender la evolución histórica de las herramientas de automatización web.

📌 Modalidad de trabajo

Este taller se puede realizar de forma individual o en grupos de máximo 3 personas.

━━━━━━━━━━━━━━━━━━
📦 Estructura del proyecto
━━━━━━━━━━━━━━━━━━

```
e2e_testing/
├── src/
│   ├── app.py              # Aplicación Flask (gestor de tareas)
│   ├── models.py           # Modelo Task con persistencia en JSON
│   └── templates/
│       └── index.html     # Plantilla HTML con data-testid
├── tests/
│   ├── conftest.py         # Fixtures para servidor y navegador
│   └── test_tareas_e2e.py  # Pruebas E2E
├── notebooks/              # Cuadernillos educativos
├── data/                   # Almacenamiento JSON de tareas
└── requirements.txt        # Dependencias
```

━━━━━━━━━━━━━━━━━━
⚙️ Parte 1 — Instalación y ejecución inicial
━━━━━━━━━━━━━━━━━━

Instalar las dependencias:

```bash
pip install -r requirements.txt
playwright install chromium
```

Levantar la aplicación manualmente para explorarla:

```bash
cd src
python app.py
```

Visita: http://localhost:5000

Interactúa con la aplicación:
- Crear tareas
- Completar tareas
- Eliminar tareas

Ejecutar las pruebas E2E iniciales:

```bash
pytest tests/ -v
```

**Observación inicial:**

Observa que todas las pruebas pasan correctamente.

**Pregunta inicial:**

¿Las pruebas realmente están verificando comportamiento útil del sistema?

━━━━━━━━━━━━━━━━━━
🔍 Parte 2 — Análisis crítico de las pruebas
━━━━━━━━━━━━━━━━━━

Responde en tu informe:

- ¿Las pruebas actuales verifican que las tareas se crean correctamente?
- ¿Qué acciones del usuario no están siendo validadas?
- ¿Qué fallos críticos de la UI podrían pasar desapercibidos?

━━━━━━━━━━━━━━━━━━
⚠️ Parte 3 — El lado oscuro de las pruebas E2E
━━━━━━━━━━━━━━━━━━

**Sabotaje controlado:**

Abre `src/app.py` y modifica la ruta `create_task` para que:
- No guarde realmente la tarea
- Devuelva el redirect sin llamar a `repo.add()`

Ejecutar nuevamente las pruebas:

```bash
pytest tests/test_tareas_e2e.py -v
```

**Analizar el resultado:**

Responde:
- ¿Los tests detectaron el error?
- ¿Por qué siguen pasando?
- ¿Qué debilidad fundamental tienen estas pruebas E2E?

━━━━━━━━━━━━━━━━━━
🔧 Parte 4 — Playwright: locators y aserciones
━━━━━━━━━━━━━━━━━━

Usando el notebook: `notebooks/02_playwright_basico.ipynb`

Escribe pruebas que:
- Verifiquen que al crear una tarea, su título aparece en la lista.
- Verifiquen que al completar una tarea, aparece el badge "✓ Completada".
- Verifiquen que al eliminar una tarea, desaparece de la lista.

Escribe estas pruebas en `tests/test_tareas_e2e.py` bajo una clase:

```python
class TestCrearTareaFuerte:
```

━━━━━━━━━━━━━━━━━━
🔧 Parte 5 — Page Object Model
━━━━━━━━━━━━━━━━━━

Usando el notebook: `notebooks/03_escenarios_usuario.ipynb`

Implementa la clase `TaskPage` como Page Object.

Reescribe las pruebas de la Parte 4 usando `TaskPage`.

Agrega un flujo completo:
- crear tarea → completarla → verificar estado → eliminarla → verificar que no existe

━━━━━━━━━━━━━━━━━━
🔧 Parte 6 — Escenarios de error y casos extremos
━━━━━━━━━━━━━━━━━━

Amplía las pruebas para cubrir:
- Intentar crear una tarea con título vacío.
- Crear tareas duplicadas.
- Verificar que la lista muestra "No hay tareas" cuando está vacía.
- Crear múltiples tareas y verificar el orden.

━━━━━━━━━━━━━━━━━━
📊 Parte 7 — Reflexión sobre pruebas E2E en CI/CD
━━━━━━━━━━━━━━━━━━

Usando el notebook: `notebooks/04_lado_oscuro_e2e.ipynb`

Responde:
- ¿Qué son los flaky tests y por qué son especialmente comunes en E2E?
- ¿Cómo garantizarías el aislamiento entre tests en una suite E2E?
- ¿En qué casos usarías E2E en lugar de pruebas de integración?

━━━━━━━━━━━━━━━━━━
📦 Entregable
━━━━━━━━━━━━━━━━━━

Debes entregar un Pull Request (PR) desde tu rama hacia la rama principal del repositorio.

📌 Flujo de entrega

**Clonar el repositorio base proporcionado por el profesor:**

```bash
git clone URL_DEL_REPOSITORIO
```

**Crear una rama de trabajo:**

El nombre de la rama debe identificar a los autores.

👤 Entrega individual

Usa el formato: `nombre_apellido1_apellido2`

Ejemplo: `andres_julian_bermudez_garcia`

👥 Entrega grupal (máximo 3 personas)

Usa los apellidos de todos los integrantes unidos por guiones bajos.

Ejemplo: `bermudez_perez_gomez`

También pueden usar: `grupo_bermudez_perez_gomez`

**Crear la rama:**

```bash
git checkout -b nombre-de-la-rama
```

**Realizar los cambios necesarios:**

Incluye:
- Nuevas pruebas
- Implementación de Page Objects
- Análisis y reflexión técnica

**Realizar commits descriptivos:**

```bash
git commit -m "feat: add robust E2E tests using Playwright"
```

**Subir la rama al repositorio remoto:**

```bash
git push origin nombre-de-la-rama
```

**Abrir el Pull Request:**

Abrir el Pull Request hacia: `main`

En la descripción del Pull Request deben aparecer:
- Nombres completos de todos los integrantes
- Código estudiantil o identificación

━━━━━━━━━━━━━━━━━━
⚠️ Nota importante
━━━━━━━━━━━━━━━━━━

Se evaluará:

- La calidad de los locators
  - Preferencia por data-testid
  - Evitar XPath frágiles

- La robustez de las aserciones
  - Verificación de estado y comportamiento
  - No solo ausencia de errores

- La correcta aplicación del Page Object Model

- El aislamiento entre tests
  - Ningún test debe depender del estado dejado por otro

- La profundidad del análisis crítico en el informe
