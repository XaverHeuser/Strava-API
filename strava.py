"""
This script is for getting activity information from Strava.
Use Case: Data Analysis
Author: Xaver Heuser (xaver.heuser@gmail.com)
Date: 14.10.2024

Link to Stra API: https://developers.strava.com/docs/reference/

"""

import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Config
with open('config.json', 'r') as f:
    config = json.load(f)

activities_url = config['links']['activities']
auth_url = config['links']['auth']

payload = {
    'client_id': config['client_id'],
    'client_secret': config['client_secret'],
    'refresh_token': config['refresh_token'],
    'grant_type': config['grant_type'],
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {} \n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}

# The first loop, request_page_number will be set to one, so it requests the first page. Increment this number after
# each request, so the next time we request the second page, then third, and so on...
request_page_num = 1
all_activities = []

while True:
    param = {'per_page': 200, 'page': request_page_num}
    # initial request, where we request the first page of activities
    my_dataset = requests.get(activities_url, headers=header, params=param).json()

    # check the response to make sure it is not empty. If it is empty, that means there is no more data left. So if you have
    # 1000 activities, on the 6th request, where we request page 6, there would be no more data left, so we will break out of the loop
    if len(my_dataset) == 0:
        break

    # if the all_activities list is already populated, that means we want to add additional data to it via extend.
    if all_activities:
        all_activities.extend(my_dataset)

    # if the all_activities is empty, this is the first time adding data so we just set it equal to my_dataset
    else:
        all_activities = my_dataset

    request_page_num += 1

print('The length of all activies is: ', len(all_activities))
for activity in all_activities:
    print(activity['name'])
    print(activity['distance']/1000, 'km')
    print(activity['elapsed_time']/60, 'min')
    print(10*'=')

