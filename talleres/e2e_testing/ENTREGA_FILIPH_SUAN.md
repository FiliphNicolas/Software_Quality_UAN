# Información de Entrega - Taller de Pruebas E2E

## Datos del Estudiante

**Nombre Completo:** Filiph Nicolas Suan Yara  
**Código Estudiantil:** 13572324996  
**Documento de Identidad (Cédula de Ciudadanía):** 1000694062  

## Rama Git

**Nombre de la rama:** `filiph_suan_yara`

## Estado del Taller

✅ **Actividades Completadas:**

1. ✅ Configuración del entorno E2E con Playwright
2. ✅ Análisis crítico de pruebas E2E iniciales
3. ✅ Sabotaje controlado de la ruta create_task
4. ✅ Implementación de pruebas fuertes con locators robustos
5. ✅ Aplicación del Page Object Model
6. ✅ Cobertura de escenarios de error y casos extremos
7. ✅ Reflexión sobre pruebas E2E en CI/CD

## Archivos Entregados

### Código Fuente
- `src/app.py` - Aplicación Flask (gestor de tareas)
- `src/models.py` - Modelo Task con persistencia en JSON
- `src/templates/index.html` - Plantilla HTML con data-testid

### Pruebas E2E
- `tests/conftest.py` - Fixtures para servidor y navegador
- `tests/test_tareas_e2e.py` - Pruebas E2E iniciales (débiles)

### Material Educativo
- `notebooks/02_playwright_basico.ipynb` - Playwright: locators y aserciones
- `notebooks/03_escenarios_usuario.ipynb` - Page Object Model
- `notebooks/04_lado_oscuro_e2e.ipynb` - Limitaciones de pruebas E2E

### Documentación
- `ENTREGABLE.md` - Instrucciones del taller

## Resumen de Aprendizajes

### Sabotaje Controlado
El sabotaje de la ruta `create_task` reveló que las pruebas E2E iniciales que solo verifican que no hay errores son extremadamente débiles. Las pruebas deben verificar el estado real del sistema después de las acciones.

### Locators Robustos
Se implementó el uso de `data-testid` en lugar de XPath frágiles, garantizando que las pruebas sean estables ante cambios en el CSS y estructura del DOM.

### Page Object Model
Se aplicó el patrón POM para encapsular la lógica de interacción con la página, mejorando la reutilización y mantenibilidad de las pruebas.

### Limitaciones de E2E
Se documentaron los desafíos de las pruebas E2E: flaky tests, dependencia del estado, lentitud, y la importancia de la pirámide de pruebas.

## Instrucciones para el Pull Request

1. Crear rama: `git checkout -b filiph_suan_yara`
2. Commit cambios: `git commit -am "Entrega taller E2E - Filiph Suan"`
3. Push a remoto: `git push origin filiph_suan_yara`
4. Crear Pull Request hacia `main`

**Descripción del PR:**
```
Entrega Taller: Pruebas E2E con Playwright

Estudiante: Filiph Nicolas Suan Yara
Código: 13572324996
Cédula: 1000694062

Actividades completadas:
- Configuración del entorno E2E
- Análisis crítico de pruebas iniciales
- Sabotaje controlado y detección de debilidades
- Implementación de pruebas fuertes con data-testid
- Aplicación del Page Object Model
- Cobertura de escenarios de error
- Reflexión sobre pruebas E2E en CI/CD
```

---

**Fecha de entrega:** 28 de mayo de 2026
