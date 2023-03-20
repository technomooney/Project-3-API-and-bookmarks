import requests
import json
from park import Park

# National Park Service API endpoint
url = 'https://developer.nps.gov/api/v1/parks'

# API key ( I stored on my pc )
api_key = 'NPS_API_KEY'

"""
Defined two separate functions: make_request() and process_data(). The make_request() function takes a state_code parameter, sends an API request to the National Park Service API,
 and returns the response as JSON. This function includes error handling for cases where the request fails or the response is not in JSON format.
"""
def make_requests(state_code):
    """ Makes an API request to the National Park Service API and returns the response as JSON."""
    params = {'api_key': api_key, 'stateCode': state_code}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise an exception if the response status code is not 200 OK
        return response.json()
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print('Error: ', e)


"""
The process_data() function takes a JSON data parameter, processes the data to create a list of Park objects, and returns the list. 
This function checks if the data parameter is not None before processing the data to avoid errors.

"""
def process_data(data):
    """Processes the JSON data returned by the National Park Service API 
    and returns a list of park objects. """
    parks = []
    if data is not None:
        for park_data in data['data']:
            park = Park(park_data['fullName'], park_data['description'])
            parks.append(park)
    return parks

"""
In the main block of the program, we call make_request() with the state_code parameter set to 'CA' to get the JSON data from the API, 
and then call process_data() with the JSON data to create a list of Park objects
"""
if __name__ == '__main__':
    data = make_requests('CA')
    if data is None:
        print('Error: Failed to retrieve park data from API.')
    else:
        parks = process_data(data)
        if len(parks) == 0:
            print('No parks found for the specified state code.')
        else:
            for park in parks:
                print(park.full_name)
                print(park.description)
                print('-------------------------')