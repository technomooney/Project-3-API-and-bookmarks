# This section imports necessary libraries requests , os , logging and pprint.

import os
import requests
from typing import List
from park import Park

base_url = 'https://developer.nps.gov/api/v1' # Sets a variable base_url to the base URL for the National Park Service API.

# The get_parks_data function is called with the specified search criteria. 
# This function constructs a URL with the API endpoint and parameters, 
# and sends a GET request to retrieve data from the API. The response data is converted to JSON format 
# and the "data" field is extracted as a list of dictionaries.

def get_parks_data(state: str, search_query: str = "", park_code: str = None, limit: int = 5) -> List[dict]:
    url = f"{base_url}/parks"
    api_key = os.getenv('NPS_API_KEY') # a GET request to the National Park Service API.
    query = {"api_key":api_key, "q": search_query, "stateCode": state, "limit": limit, "parkCode": park_code}
    response = requests.get(url, params=query)
    response_data = response.json()
    return response_data.get("data", [])

# The process_parks_data function is called with the list of dictionaries returned by get_parks_data.
#  This function iterates over each dictionary and creates a Park object for each one.
#  The Park object is initialized with the "parkCode" and "fullName" fields,
#  and other relevant fields are assigned if they exist in the dictionary. The Park object is added to a list of Park objects.

def process_parks_data(parks_data: List[dict]) -> list[Park]:
    parks = []
    for park_data in parks_data:
        park = Park(park_data["parkCode"], parks_data["fullName"])
        park.description = park_data.get("description")
        park.lat = park_data.get("latitude")
        park.lon = park_data.get("longitude")
        contacts = park_data.get("contacts", [])
        if contacts:
            phone_numbers = contacts[0].get("phoneNumbers", [])
            if phone_numbers:
                park.phone = phone_numbers[0].get("phoneNumber")
            email_addresses = contacts[0].get("emailAddresses", [])
            if email_addresses:
                park.email = email_addresses[0].get("emailAddress")
        park.entrance_fees = park_data.get("entranceFees")
        park.entrance_passes = park_data.get("entrancePasses")
        park.operating_hours = park_data.get("operatingHours")
        parks.append(park)
    return parks
# The get_parks function is called with the specified search criteria. 
# This function calls get_parks_data to retrieve the data, and then calls process_parks_data to create a list of Park objects. 
# The list of Park objects is returned as the function result.

def get_parks(state: str, search_query: str = "", park_code: str = None, limit: int = 5) -> List[Park]:
    parks_data = get_parks_data(state, search_query, park_code, limit)
    parks = process_parks_data(parks_data)
    return parks
