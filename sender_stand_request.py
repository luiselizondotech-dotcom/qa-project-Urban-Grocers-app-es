
import requests
import configuration
import data



def get_new_user_token():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body
    )

    if response.status_code == 201:
        return response.json().get("authToken")
    else:

        return None




def post_new_client_kit(kit_body, auth_token):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        headers=headers,
        json=kit_body
    )
    return response

