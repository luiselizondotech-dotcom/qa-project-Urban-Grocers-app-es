# 🛒 Urban Grocers — API Test Automation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pytest](https://img.shields.io/badge/Pytest-latest-green)
![Requests](https://img.shields.io/badge/Requests-HTTP-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Contexto del Negocio

Urban Grocers es una aplicación de pedidos de abarrotes en línea que permite a los usuarios crear kits de productos personalizados. En plataformas de e-commerce, la integridad de los datos enviados a través de la API es fundamental — un campo `name` sin validación correcta puede causar errores en base de datos, experiencias rotas para el usuario y vulnerabilidades de seguridad.

Este proyecto automatiza la validación del endpoint de creación de kits, asegurando que la API se comporte correctamente ante todo tipo de entrada de datos.

---

## 🎯 Objetivo

Validar mediante pruebas automatizadas el endpoint `POST /api/v1/kits` de Urban Grocers, aplicando técnicas de **clases de equivalencia y valores límite** sobre el campo `name` para garantizar la robustez de la API.

---

## 🧪 Casos de Prueba Automatizados

| # | Escenario | Entrada | Resultado Esperado |
|---|-----------|---------|-------------------|
| 1 | Nombre mínimo válido | `"a"` (1 carácter) | 201 Created |
| 2 | Nombre máximo válido | 511 caracteres | 201 Created |
| 3 | Nombre vacío | `""` (0 caracteres) | 400 Bad Request |
| 4 | Nombre excede límite | 512 caracteres | 400 Bad Request |
| 5 | Caracteres especiales permitidos | `"!№%@"` | 201 Created |
| 6 | Espacios permitidos | `" A Aaa "` | 201 Created |
| 7 | Números como string permitidos | `"123"` | 201 Created |
| 8 | Campo name ausente | `{}` | 400 Bad Request |
| 9 | Tipo de dato incorrecto | `{"name": 123}` (entero) | 400 Bad Request |

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Propósito |
|-------------|-----------|
| Python 3.x | Lenguaje principal |
| Requests | Peticiones HTTP a la API |
| Pytest | Framework de pruebas, fixtures y aserciones |
| configuration.py | Gestión de URL y rutas del entorno |

---

## 📁 Estructura del Proyecto
```
qa-project-Urban-Grocers-app-es/
├── create_kit_name_kit_test.py  # Casos de prueba automatizados
├── sender_stand_request.py      # Funciones para llamadas a la API
├── configuration.py             # URL del servidor y configuración
├── data.py                      # Datos de prueba y factory functions
├── README.md
└── .gitignore
```

---

## 🚀 Cómo Ejecutar las Pruebas

### 1. Clonar el repositorio
```bash
git clone https://github.com/luiselizondotech-dotcom/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Instalar dependencias
```bash
pip install requests pytest
```

### 4. Configurar el servidor

Inicia el servidor en TripleTen y actualiza la URL en `configuration.py`:
```python
URL_SERVICE = "https://tu-servidor-urban-grocers.containerhub.tripleten-services.com"
```

> ⚠️ La URL cambia cada vez que reinicias el servidor. Actualízala antes de ejecutar las pruebas.

### 5. Ejecutar las pruebas
```bash
pytest create_kit_name_kit_test.py -v
```

---

## ✅ Resultados y Conclusiones

1. **Validación correcta de límites** — La API responde con `201 Created` dentro de los rangos permitidos y `400 Bad Request` fuera de ellos.
2. **Bugs detectados** — 4 casos negativos devuelven respuestas inesperadas, evidenciando defectos reales en la validación de la API.
3. **Velocidad de regresión** — La automatización redujo el tiempo de ejecución de estas pruebas de minutos a segundos.
4. **Valor al negocio** — Una API con validaciones sólidas previene errores en producción y protege la integridad de los datos del usuario.

---

## 👤 Autor

**Luis Elizondo** — QA Engineer