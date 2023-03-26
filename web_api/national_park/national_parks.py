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