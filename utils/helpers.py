"""
Example documentation ...
"""

import json


################################
# Read Config File
################################

def load_config(file_path='config.json'):
    """Load configuration from a JSON file."""
    with open(file_path, 'r') as f:
        config = json.load(f)

    activities_url = config['links']['activities']
    auth_url = config['links']['auth']

    return activities_url, auth_url, config