import json
import requests
from dotenv import dotenv_values
import os
from utils import *

# Get current file path
current_file_path = os.path.abspath(__file__)
# get the root directory path
root_directory = os.path.dirname(current_file_path)
env_file_path = os.path.join(root_directory, '.env')
env_vars = dotenv_values(env_file_path)
api_token = env_vars['API_TOKEN']

base_url = "https://gorest.co.in"

id_list = []


def create_users():
    """
        Creates a new user by sending a POST request to an API endpoint.

        Returns:
            str: The response body in JSON format.
            list: A list containing user information[id].

        Raises:
            AssertionError: If the status code of the response is not 201.

        """
    api_url = base_url + "/public/v2/users/"
    user_headers = {"Authorization": "Bearer " + api_token}

    # payload
    user_payload = {
        "name": random_name(4),
        "email": random_email(5),
        "gender": "male",
        "status": "active"
    }

    response = requests.post(api_url, json=user_payload, headers=user_headers)

    # verify status code
    try:
        assert response.status_code == 201
        print("Get Response Status Code passed: ", response.status_code)
    except Exception as e:
        print("Get Response Status Code Exception: " + type(e).__name__)

    # Store id in list
    json_body = response.json()
    id_list.append(json_body['id'])
    print("ID List: ", id_list)

    # get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)
    print("Response: " + json_data)
    return json_data


for _ in range(2):
    create_users()
