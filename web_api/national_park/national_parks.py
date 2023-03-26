import requests #import the requests 
import os # import the os 

# A Park class to represent information about a park.

class Park:
    def __init__(self, name, description, state_code, location, park_code, phone, email):
        self.name =  name
        self.description = description
        self.state_code = state_code
        self.location = location
        self.park_code = park_code
        self.phone = phone
        self.email = email

# Creating a function to search for parks based on a query
def search_parks(query):
    # Set the API URL
    url = 'https://developer.nps.gov/api/v1/parks'
    # Set the query parameters
    params = {
        'q': query, # The search query
        'fields': 'images', 
        'api_key': os.environ.get('NPS_API_KEY') #The API key (I got the key stored on my pc)
    }
    #Send a GET request to the API with the query parameters
    response = requests.get(url, params=params)
    
    response.raise_for_status() # Raise an exception if the response status code is not 200 OK

    data = response.json() # Parse the response data as JSON

    # Create a list to store Park objects for each park in the search results.
    parks = [] 
    