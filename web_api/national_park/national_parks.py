import requests
import os
from park import Park

api_key = os.environ.get('NPS_API_KEY')
url = 'https://developer.nps.gov/api/v1/parks'


def get_parks_data(query):
    """GET request from NPS API using the search query given when the function is called.
    Turns response into JSON and catches any exceptions that are raised. Returns data/None
    if there aren't any errors, and None/exception if there are any errors."""
    try:
        params = {'q': query, 'api_key': api_key}
        response = requests.get(url, params=params) # Send a GET request to the API with the query parameters
        response.raise_for_status() # Raise an exception if the response status code is not 200 OK
        response_json = response.json() # Parse the response data as JSON
        park_data = response_json.get('data')
        return park_data, None # Return the data/None if there aren't any exceptions raised
    except Exception as ex:
        return None, ex # If an exceptions occur, return None instead of data, and the exception


def create_park_objects_list(data):
    """Create a Park object out of each object in the API response containing the park's
    name, description, state_code, location, park_code, phone, and email. 
    The function returns a list of park objects."""
    park_data, error = data # Unpack tuple that holds either data or exception
    parks = [] # Store park objects
    
    for park in park_data:  # Create a park object for each set of results and add to the park list 
        name = park['fullName'],
        description = park['description'],
        state_code = park['states'],
        latitude = park['latitude']
        longitude = park['longitude']
        park_code = park['parkCode'],
        phone = park['contacts']['phoneNumbers'][0]['phoneNumber'],
        email = park['contacts']['emailAddresses'][0]['emailAddress']

        park = Park(name, description, state_code, latitude, longitude, park_code, phone, email)
        parks.append(park)

    return parks    