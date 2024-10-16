"""
Example Text ...
"""

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_access_token(auth_url, client_id, client_secret, refresh_token, grant_type):
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': grant_type,
        'f': 'json'
    }

    try:
        response = requests.post(auth_url, data=payload, verify=False)
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
