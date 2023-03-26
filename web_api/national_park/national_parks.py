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

    # loop through each park in the search results.
    for park_data in data['data']:
        # Create a park object for the park and add it to the park list 
        park = Park(
            name=park_data['fullName'],
            description=park_data['description'],
            state_code=park_data['stateCode'],
            location=park_data['latLong'],
            park_code=park_data['parkCode'],
            phone=park_data['contacts']['phoneNumbers'][0]['phoneNumber'],
            email=park_data['contacts']['emailAddresses'][0]['emailAddress']
        )
        parks.append(park)

    # Return the list Park objects
    return parks

# A function to select a park from a list of parks
def select_parks(parks):

    # Display a numbered list of parks
    print("Please select a park:")
    for i, park in enumerate(parks):
        print(f"{i+1}. {park.name} ({park.state_code})")
    # Loop until select a valid park
    while True:
        # Enter a park number in the program to choice
        choice = input("Enter park number:")
        try:
            index = int(choice) - 1 # convert the input to an index
            # if the index is within the range of the parks list, return the selected park
            if 0 <= index < len(parks):
                return parks[index]
        except ValueError:
            pass
        # if the input is invalid, display an error message.
        print("Invalid input, please try again. ")
        

    