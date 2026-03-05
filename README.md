# 🛒 Urban Grocers — API Test Automation

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Latest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-FF6C37?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## 📌 Contexto del Negocio

**Urban Grocers** es una aplicación de pedidos de abarrotes en línea que permite a los usuarios crear kits de productos personalizados. En plataformas de e-commerce, la integridad de los datos enviados a través de la API es fundamental — un campo `name` sin validación correcta puede causar errores en base de datos, experiencias rotas para el usuario y vulnerabilidades de seguridad.

Este proyecto automatiza la validación del endpoint de creación de kits, asegurando que la API se comporte correctamente ante todo tipo de entrada de datos.

---

## 🎯 Objetivo

Validar mediante pruebas automatizadas el endpoint `POST /api/v1/kits` de Urban Grocers, aplicando técnicas de **clases de equivalencia y valores límite** sobre el campo `name` para garantizar la robustez de la API.

---

## 🧪 Casos de Prueba Automatizados

| # | Escenario | Entrada | Resultado Esperado |
|---|-----------|---------|-------------------|
| 1 | Nombre mínimo válido | 1 carácter | 201 Created |
| 2 | Nombre máximo válido | 511 caracteres | 201 Created |
| 3 | Nombre con caracteres especiales | `@#$%` | 201 Created |
| 4 | Nombre con espacios | `" "` | 201 Created |
| 5 | Nombre vacío | `""` | 400 Bad Request |
| 6 | Nombre con valor numérico | `123` | 400 Bad Request |
| 7 | Nombre excede límite | 512+ caracteres | 400 Bad Request |
| 8 | Campo name ausente | Sin campo | 400 Bad Request |
| 9 | Tipo de dato incorrecto | `true` / `null` | 400 Bad Request |

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Propósito |
|-------------|-----------|
| Python 3.x | Lenguaje principal |
| Requests | Peticiones HTTP a la API |
| Pytest | Framework de pruebas y aserciones |
| configuration.py | Gestión de URL y configuración del entorno |

---

## 📁 Estructura del Proyecto
```
qa-project-Urban-Grocers-app-es/
├── create_kit_name_kit_test.py  # Casos de prueba automatizados
├── sender_stand_request.py      # Funciones para llamadas a la API
├── configuration.py             # URL del servidor y configuración
├── data.py                      # Datos de prueba
└── README.md
```

---

## 🚀 Cómo Ejecutar las Pruebas

**1. Clonar el repositorio**
```bash
git clone https://github.com/luiselizondotech-dotcom/qa-project-Urban-Grocers-app-es.git
cd qa-project-Urban-Grocers-app-es
```

**2. Instalar dependencias**
```bash
pip install requests pytest
```

**3. Configurar el servidor**

Abre `configuration.py` y actualiza la URL de tu servidor:
```python
URL_SERVICE = "https://tu-servidor-urban-grocers.com"
```

**4. Ejecutar las pruebas**
```bash
pytest -v
```

---

## ✅ Resultados y Conclusiones

1. **Validación correcta de límites** — La API responde con `201 Created` dentro de los rangos permitidos y `400 Bad Request` fuera de ellos, alineado con la documentación técnica.
2. **Cobertura de casos negativos** — Se validaron campos vacíos, tipos incorrectos y valores fuera de límite, cubriendo los escenarios de mayor riesgo.
3. **Velocidad de regresión** — La automatización redujo el tiempo de ejecución de estas pruebas de minutos a segundos.
4. **Valor al negocio** — Una API con validaciones sólidas previene errores en producción, reduce costos de soporte y protege la integridad de los datos del usuario.

---

## 👤 Autor

**Luis Elizondo** — QA Engineer  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/qa-engineer-elizondo-luis/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/luiselizondotech-dotcom)
