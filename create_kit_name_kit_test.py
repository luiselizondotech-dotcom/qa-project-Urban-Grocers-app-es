# create_kit_name_kit_test.py
import pytest
import sender_stand_request
import data


# --- Fixture: genera un token nuevo para toda la sesión de pruebas ---
@pytest.fixture(scope="session")
def auth_token():
    return sender_stand_request.get_new_user_token()


# --- Aserciones reutilizables ---
def positive_assert(kit_body, auth_token):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201, (
        f"Se esperaba 201 pero se obtuvo {kit_response.status_code}\n"
        f"Body: {kit_response.text}"
    )
    assert kit_response.json()["name"] == kit_body["name"], (
        f"El nombre en la respuesta no coincide.\n"
        f"Esperado: {kit_body['name']}\n"
        f"Obtenido: {kit_response.json()['name']}"
    )
    assert kit_response.elapsed.total_seconds() < 2.0, (
        f"La API tardó más de 2 segundos: {kit_response.elapsed.total_seconds()}s"
    )


def negative_assert_code_400(kit_body, auth_token):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400, (
        f"Se esperaba 400 pero se obtuvo {kit_response.status_code}\n"
        f"Body: {kit_response.text}"
    )


# --- Pruebas de la Lista de Comprobación ---

# 1. El número permitido de caracteres (1)
def test_create_kit_1_char_name(auth_token):
    kit_body = data.get_kit_body("a")
    positive_assert(kit_body, auth_token)


# 2. El número permitido de caracteres (511)
def test_create_kit_511_char_name(auth_token):
    kit_body = data.get_kit_body(data.kit_name_511_chars)
    positive_assert(kit_body, auth_token)


# 3. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_char_name(auth_token):
    kit_body = data.get_kit_body("")
    negative_assert_code_400(kit_body, auth_token)


# 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_char_name(auth_token):
    kit_body = data.get_kit_body(data.kit_name_512_chars)
    negative_assert_code_400(kit_body, auth_token)


# 5. Se permiten caracteres especiales
def test_create_kit_special_chars_name(auth_token):
    kit_body = data.get_kit_body("!№%@")
    positive_assert(kit_body, auth_token)


# 6. Se permiten espacios
def test_create_kit_spaces_name(auth_token):
    kit_body = data.get_kit_body(" A Aaa ")
    positive_assert(kit_body, auth_token)


# 7. Se permiten números como string
def test_create_kit_numbers_name(auth_token):
    kit_body = data.get_kit_body("123")
    positive_assert(kit_body, auth_token)


# 8. El parámetro name no se pasa en la solicitud
def test_create_kit_no_name_field(auth_token):
    kit_body = {}
    negative_assert_code_400(kit_body, auth_token)


# 9. Se pasa un tipo de dato incorrecto (número entero en lugar de string)
def test_create_kit_number_type_name(auth_token):
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body, auth_token)