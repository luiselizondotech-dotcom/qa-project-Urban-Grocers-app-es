
import sender_stand_request
import data


AUTH_TOKEN = sender_stand_request.get_new_user_token()




# Asersión para pruebas positivas (Código 201)
def positive_assert(kit_body):
    # 1. Ejecutar la solicitud
    kit_response = sender_stand_request.post_new_client_kit(kit_body, AUTH_TOKEN)

    # 2. Comprobar que el código de respuesta es 201
    assert kit_response.status_code == 201

    # 3. Comprobar que el nombre del kit en la respuesta coincide con el enviado
    assert kit_response.json()["name"] == kit_body["name"]


# Asersión para pruebas negativas (Código 400)
def negative_assert_code_400(kit_body):
    # 1. Ejecutar la solicitud
    kit_response = sender_stand_request.post_new_client_kit(kit_body, AUTH_TOKEN)

    # 2. Comprobar que el código de respuesta es 400
    assert kit_response.status_code == 400


# --- Pruebas de la Lista de Comprobación ---

# 1. El número permitido de caracteres (1)
def test_create_kit_1_char_name():
    kit_body = data.get_kit_body("a")
    positive_assert(kit_body)


# 2. El número permitido de caracteres (511)
def test_create_kit_511_char_name():
    kit_body = data.get_kit_body(data.kit_name_511_chars)
    positive_assert(kit_body)


# 3. El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_char_name():
    kit_body = data.get_kit_body("")
    negative_assert_code_400(kit_body)


# 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_char_name():
    kit_body = data.get_kit_body(data.kit_name_512_chars)
    negative_assert_code_400(kit_body)


# 5. Se permiten caracteres especiales: !№%@
def test_create_kit_special_chars_name():
    kit_body = data.get_kit_body("!№%@")
    positive_assert(kit_body)


# 6. Se permiten espacios: " A Aaa "
def test_create_kit_spaces_name():
    kit_body = data.get_kit_body(" A Aaa ")
    positive_assert(kit_body)


# 7. Se permiten números: 123
def test_create_kit_numbers_name():
    kit_body = data.get_kit_body("123")
    positive_assert(kit_body)


# 8. El parámetro no se pasa en la solicitud: {}
# Esto debe probarse enviando un cuerpo de solicitud vacío o sin el campo "name"
def test_create_kit_no_name_field():
    kit_body = {}
    negative_assert_code_400(kit_body)  # Se espera 400 por validación de nombre


# 9. Se ha pasado un tipo de parámetro diferente (número): 123
def test_create_kit_number_type_name():
    kit_body = {"name": 123}  # El nombre es un número, no una cadena
    negative_assert_code_400(kit_body)  # Se espera 400 por validación de tipo
