# Información de Entrega - Taller de Pruebas de Integración

## Datos del Estudiante

**Nombre Completo:** Filiph Nicolas Suan Yara  
**Código Estudiantil:** 13572324996  
**Documento de Identidad (Cédula de Ciudadanía):** 1000694062  

## Rama Git

**Nombre de la rama:** `filiph_suan_yara`

## Estado del Taller

✅ **Actividades Completadas:**

1. ✅ Análisis inicial de pruebas de integración existentes
2. ✅ Sabotaje controlado del método add_task
3. ✅ Aplicación de enfoque Top-Down con stubs
4. ✅ Aplicación de enfoque Bottom-Up con drivers
5. ✅ Aplicación de enfoque Sandwich (híbrido)
6. ✅ Mejora de cobertura de integración
7. ✅ Documentación de reflexión técnica

## Archivos Entregados

### Código Fuente
- `src/service.py` - Módulo de servicio con lógica de integración
- `src/storage.py` - Módulo de almacenamiento
- `src/notifier.py` - Módulo de notificaciones

### Pruebas (48 tests, todos pasando)
- `tests/test_integration.py` - Pruebas iniciales de integración
- `tests/test_topdown.py` - Pruebas Top-Down con stubs
- `tests/test_bottomup.py` - Pruebas Bottom-Up con drivers
- `tests/test_sandwich.py` - Pruebas Sandwich híbridas
- `tests/test_integration_improved.py` - Pruebas con cobertura mejorada

### Material Educativo
- `notebooks/01_stubs_and_drivers.ipynb` - Explicación de stubs y drivers
- `notebooks/02_integration_strategies.ipynb` - Estrategias de integración
- `notebooks/03_sabotage_controlled.ipynb` - Ejemplos de sabotaje controlado
- `notebooks/04_best_practices.ipynb` - Buenas prácticas de testing

### Documentación
- `ENTREGABLE.md` - Instrucciones del taller
- `REFLEXION_TECNICA.md` - Reflexión sobre cobertura de código vs integración

## Resultados de Pruebas

```
pytest tests/ -v
======================================= 48 passed in 0.55s =======================================
```

## Resumen de Aprendizajes

### Sabotaje Controlado
El sabotaje del método `add_task` reveló que las pruebas iniciales que solo verifican el valor de retorno son débiles y pueden ser engañadas por código malicioso. Las pruebas mejoradas ahora verifican las interacciones reales entre componentes.

### Estrategias de Integración Aplicadas
- **Top-Down**: Validación de lógica de alto nivel con stubs
- **Bottom-Up**: Validación de componentes básicos con drivers
- **Sandwich**: Combinación de componentes reales y stubs para máxima cobertura

### Cobertura vs Calidad
Se documentó la diferencia fundamental entre cobertura de código (métrica cuantitativa) y cobertura de integración (métrica cualitativa), demostrando que alta cobertura de código no garantiza pruebas efectivas.

## Instrucciones para el Pull Request

1. Crear rama: `git checkout -b filiph_suan_yara`
2. Commit cambios: `git commit -am "Entrega taller integración - Filiph Suan"`
3. Push a remoto: `git push origin filiph_suan_yara`
4. Crear Pull Request hacia `main`

**Descripción del PR:**
```
Entrega Taller: Pruebas de Integración

Estudiante: Filiph Nicolas Suan Yara
Código: 13572324996
Cédula: 1000694062

Actividades completadas:
- Análisis crítico de pruebas existentes
- Sabotaje controlado y detección de debilidades
- Implementación de pruebas Top-Down con stubs
- Implementación de pruebas Bottom-Up con drivers
- Implementación de pruebas Sandwich híbridas
- Mejora de cobertura de integración (48 tests)
- Documentación de reflexión técnica

Todos los tests pasan: 48/48
```

---

**Fecha de entrega:** 27 de mayo de 2026
