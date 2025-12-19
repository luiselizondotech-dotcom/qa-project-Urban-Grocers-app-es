# qa-project-Urban-Grocers-app-es

## Descripción del Proyecto
Este proyecto contiene pruebas de automatización para la API de Urban Grocers, enfocándose en la funcionalidad de **crear un kit** y validar los límites y tipos de datos del campo `name` según la lista de comprobación de pruebas.

---

## 📊 Análisis de Pruebas y Metodología
Para este proyecto, se realizó un análisis de **clases de equivalencia y valores límite** sobre el endpoint de creación de kits. Se diseñaron 9 casos de prueba automatizados que cubren:
- **Valores límite:** Nombres de kit con 1 carácter (mínimo) y 511 caracteres (máximo).
- **Tipos de datos:** Validación de manejo de caracteres especiales, espacios y valores numéricos.
- **Validación de errores:** Comportamiento de la API ante campos vacíos o tipos de datos incorrectos (ej. números en lugar de strings).

### 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Librerías:** `requests` para peticiones HTTP.
* **Framework:** `pytest` para la ejecución y aserciones.

---

## ✅ Conclusiones y Resultados
Tras la ejecución de la suite de pruebas, se concluye que:
1. La API responde correctamente con el código de estado **201 Created** cuando se cumplen los requisitos del esquema.
2. Los mensajes de error y códigos **400 Bad Request** están alineados con la documentación técnica cuando se ingresan datos fuera de los límites permitidos.
3. La automatización permite reducir el tiempo de regresión de estas funcionalidades de minutos a solo segundos.


---

## ⚙️ Reglas/Pasos para Ejecutar las Pruebas

1. **Iniciar el Servidor de Urban Grocers:** Asegúrate de que tu servidor de pruebas esté activo.
2. **Actualizar la Configuración:** Abre el archivo `configuration.py` y actualiza el valor de `URL_SERVICE`.
3. **Ejecutar Pytest:** ```bash
   pytest
