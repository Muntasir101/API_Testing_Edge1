import json
import requests
from utils import *


def create_users():
    """
    Create a new user by sending a POST request to the API endpoint.

    Returns:
        str: The response body in JSON format.

    Raises:
        AssertionError: If the status code of the response is not 201.
    """
    # Load API token from environment variables
    api_token = load_api_token()

    # API endpoint for creating users
    api_url = "https://gorest.co.in/public/v2/users/"

    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    # Payload for creating a user
    user_payload = {
        "name": random_name(4),
        "email": random_email(5),
        "gender": "male",
        "status": "active"
    }

    # Send POST request to the API endpoint
    response = requests.post(api_url, json=user_payload, headers=headers)
    response.raise_for_status()

    # Verify the status code of the response
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"

    # get response body
    json_body = response.json()
    print("Response: ")
    print(json.dumps(json_body, indent=4))

    # Extract the 'id' value from the response
    user_id = response.json()["id"]

    # Print user information
    print(f"User created successfully. ID: {user_id}")

    # Return the response body in JSON format
    return json.dumps(response.json(), indent=4)


create_users()
