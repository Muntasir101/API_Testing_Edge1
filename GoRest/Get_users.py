import json
import requests
from dotenv import dotenv_values
import os

# Get current file path
current_file_path = os.path.abspath(__file__)
# get the root directory path
root_directory = os.path.dirname(current_file_path)
env_file_path = os.path.join(root_directory, '.env')
env_vars = dotenv_values(env_file_path)
api_token = env_vars['API_TOKEN']

base_url = "https://gorest.co.in"


def get_all_users():
    """
            Retrieves a list of all users from an API endpoint.

            Returns:
                str: The response body in JSON format.

            Raises:
                requests.exceptions.HTTPError: If there is an error in the HTTP request.

            """
    api_url = base_url + "/public/v2/users/"
    user_headers = {"Authorization": "Bearer " + api_token}
    response = requests.get(api_url, headers=user_headers)

    # verify status code
    try:
        assert response.status_code == 200
        print("Get Response Status Code passed: ", response.status_code)
    except Exception as e:
        print("Get Response Status Code Exception: " + type(e).__name__)

    # get response body
    json_body = response.json()
    json_data = json.dumps(json_body, indent=4)
    print("Response: " + json_data)

    return json_data


get_all_users()
