# sender_stand_request.py
import requests
import configuration
import data


def get_new_user_token():
    try:
        response = requests.post(
            configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
            json=data.user_body,
            timeout=10
        )
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            f"No se pudo conectar al servidor: {configuration.URL_SERVICE}\n"
            f"¿Está levantado el servidor?"
        )
    except requests.exceptions.Timeout:
        raise TimeoutError("El servidor tardó más de 10 segundos en responder")

    assert response.status_code == 201, (
        f"Fallo al crear usuario.\n"
        f"Status: {response.status_code}\n"
        f"Body: {response.text}"
    )

    token = response.json().get("authToken")
    assert token is not None, "La respuesta no contiene el campo 'authToken'"

    return token


def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    try:
        response = requests.post(
            configuration.URL_SERVICE + configuration.KITS_PATH,
            headers=headers,
            json=kit_body,
            timeout=10
        )
        return response
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            f"No se pudo conectar al servidor: {configuration.URL_SERVICE}\n"
            f"¿Está levantado el servidor?"
        )
    except requests.exceptions.Timeout:
        raise TimeoutError("El servidor tardó más de 10 segundos en responder")