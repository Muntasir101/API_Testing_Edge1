import random
import string
from dotenv import dotenv_values
import os


def random_email(length):
    domain_name = ['gmail', 'yahoo', 'icloud', 'hotmail']
    postfix = ['.com', '.org', '.bd', '.edu']
    characters = string.ascii_letters + string.digits
    domain_select = random.choice(domain_name)
    postfix_select = random.choice(postfix)
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting + "@" + domain_select + postfix_select


def random_name(length):
    characters = string.ascii_letters + string.digits
    domain_select = random.choice(characters)
    random_sting = ''.join(random.choice(characters) for _ in range(length))
    return random_sting + domain_select


def load_api_token():
    """
    Load the API token from the environment variables.

    Returns:
        str: The API token.
    """
    current_file_path = os.path.abspath(__file__)
    root_directory = os.path.dirname(current_file_path)
    env_file_path = os.path.join(root_directory, ".env")
    env_vars = dotenv_values(env_file_path)
    api_token = env_vars.get("API_TOKEN")

    if not api_token:
        raise ValueError("API_TOKEN not found in .env file.")

    return api_token
