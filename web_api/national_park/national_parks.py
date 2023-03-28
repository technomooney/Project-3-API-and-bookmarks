import requests
import os
from .park import Park # remove the . from the "from .park import Park" statement if you plan on testing as a standalone file. 
                                # (not importing the file into another module)

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


def create_park_objects_list(park_data):
    """Create a Park object out of each object in the API response containing the park's
    name, description, state_code, location, park_code, phone, and email. 
    The function returns a list of park objects."""
    parks = [] # Store park objects
    
    for park in park_data:  # Create a park object for each set of results and add to the park list 
        name = park.get('fullName')
        description = park.get('description')
        state_code = park.get('states')
        latitude = park.get('latitude')
        longitude = park.get('longitude')
        park_code = park.get('parkCode')
        try:
            phone = park.get('contacts').get('phoneNumbers')[0].get('phoneNumber')
        except IndexError:
            phone = None
        try:
            email = park.get('contacts').get('emailAddresses')[0].get('emailAddress')
        except IndexError:
            email = None
        park = Park(name, description, state_code, latitude, longitude, park_code, phone, email)
        parks.append(park)

    return parks    

# test as a standalone file. 
if __name__ == '__main__':
    data,error = get_parks_data('yellowstone')
    park_list = create_park_objects_list(data)
    print(park_list)
