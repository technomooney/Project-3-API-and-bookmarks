# This section imports necessary libraries requests , os , logging and pprint.

import requests
import os
import logging
from pprint import pprint

base_url = 'https://developer.nps.gov/api/v1' # Sets a variable base_url to the base URL for the National Park Service API.

def park_data_collection(state, search_query="", park_code=None, limit=5):
    url = base_url + "/parks"
    parks_data_list = [] # it initializes an empty list called parks_data_list and sends 
    api_key = os.getenv('NPS_API_KEY') # a GET request to the National Park Service API.
    query = {"api_key": api_key, "q": search_query, "stateCode": state, "limit": limit, "parkCode": park_code} 
    response = requests.get(url, params=query)
    response_data = response.json()

# It then loops through the response data, creating a new Park instance for each park and populating its attributes 
# with the appropriate data. 

    for park in response_data["data"]:
        new_park = Park(park["parkCode"], park["fullName"])
        new_park.description = park.get("description")
        new_park.lat = park.get("latitude")
        new_park.lon = park.get("longitude")
        new_park.phone = park.get("contacts")[0].get("phoneNumbers")[0].get("phoneNumber")
        new_park.email = park.get("contacts")[0].get("emailAddresses")[0].get("emailAddress")
        new_park.entrance_fees = park.get("entrancePasses")
        new_park.entrance_passes = park.get("entrancePasses")
        new_park.operating_hours = park.get("operatingHours")
        
# It then appends the Park instance to the parks_data_list and returns it.
        parks_data_list.append(new_park)

    return parks_data_list    
