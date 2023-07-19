import json
import requests
from dotenv import dotenv_values
import os
from utils import *


def get_all_users():
    """
    Retrieves a list of all users from an API endpoint.

    Returns:
        str: The response body in JSON format.
        list: A list containing user information [id].

    Raises:
        requests.exceptions.HTTPError: If there is an error in the HTTP request.
    """
    api_token = load_api_token()

    base_url = "https://gorest.co.in"
    api_url = f"{base_url}/public/v2/users/"

    user_headers = {"Authorization": f"Bearer {api_token}"}

    response = requests.get(api_url, headers=user_headers)
    response.raise_for_status()

    print("Get Response Status Code passed:", response.status_code)

    json_body = response.json()
    print("Response:")
    print(json.dumps(json_body, indent=4))

    id_list = [item["id"] for item in json_body]
    print("ID List:", id_list)

    return json_body


get_all_users()
