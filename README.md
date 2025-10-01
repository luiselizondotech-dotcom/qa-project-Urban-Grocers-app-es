# qa-project-Urban-Grocers-app-es

## Descripción del Proyecto

Este proyecto contiene pruebas de automatización para la API de Urban Grocers, enfocándose en la funcionalidad de **crear un kit** y validar los límites y tipos de datos del campo `name` según la lista de comprobación de pruebas.

## Requisitos

* Python 3.x
* Librería `requests` (`pip install requests`)
* Framework de pruebas `pytest` (`pip install pytest`)

## Reglas/Pasos para Ejecutar las Pruebas

1.  **Iniciar el Servidor de Urban Grocers:**
    Asegúrate de que tu servidor de pruebas esté activo.

2.  **Actualizar la Configuración:**
    Abre el archivo `configuration.py` y **actualiza el valor de `URL_SERVICE`** con la URL activa de tu servidor (por ejemplo, la URL proporcionada: `https://cnt-70034695-9472-4ce1-ae32-180327e8f99e.containerhub.tripleten-services.com`).

3.  **Ejecutar Pytest:**
    Abre la terminal en el directorio raíz del proyecto y ejecuta el siguiente comando:

    ```bash
    pytest
    ```

    Pytest buscará las pruebas en el archivo `create_kit_name_kit_test.py` (ya que tiene el sufijo `_test`) y reportará los resultados.
