from utils.helpers import load_config, get_access_token, make_request
import json
import requests


config_path = 'C:/Users/Xaver/Xaver/Programmieren/Strava/config.json'


def get_data_activities(params=None):
    """Fetch a list of activities."""
    config = load_config(config_path)
    access_token = get_access_token(config)

    # Validate the URL
    activities_url = config['urls']['activities']
    if not activities_url:
        print("Error: Invalid activities URL in config")
        return None

    # Use the helper function to make the request
    return make_request(activities_url, access_token, params)


def get_activity_by_id(activity_id, params=None):
    """Fetch a specific activity by its ID."""
    config = load_config(config_path)
    access_token = get_access_token(config)

    # Construct the URL for the specific activity
    activities_url = f"{config['urls']['one_activity']}/{activity_id}"
    if not activities_url:
        print("Error: Invalid activities URL in config")
        return None

    # Use the helper function to make the request
    return make_request(activities_url, access_token, params)
