"""
Example documentation ...
"""

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


################################
# Read Config File
################################
def load_config(file_path='config.json'):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as f:
        config = json.load(f)

    return config


################################
# Authentication
################################
def get_access_token(config):
    payload = {
        'client_id': config['client_id'],
        'client_secret': config['client_secret'],
        'refresh_token': config['refresh_token'],
        'grant_type': config['grant_type'],
        'f': 'json'
    }

    try:
        response = requests.post(config['urls']['auth'], data=payload, verify=False)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        token = response.json().get('access_token')

        if not token:
            raise ValueError("No access token returned.")

        return token

    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


################################
# Request
################################
def make_request(url, access_token, params=None):
    """
    Helper function to make a GET request with proper error handling.
    """
    header = {'Authorization': 'Bearer ' + access_token}

    try:
        response = requests.get(url, headers=header, params=params, timeout=10)

        # Check the status code for the response
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code} - {response.reason}")
            return None

        # Try to parse the response as JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            print("Error: Failed to decode the response as JSON")
            return None

    except requests.exceptions.Timeout:
        print("Error: The request timed out")
        return None

    except requests.exceptions.RequestException as e:
        # Catch all other request-related exceptions
        print(f"Error: An error occurred while making the request - {e}")
        return None
