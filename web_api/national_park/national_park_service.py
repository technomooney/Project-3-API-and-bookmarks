import requests,os,logging
from pprint import pprint

base_url = 'https://developer.nps.gov/api/v1'

class Park():
    def __init__(self,park_code,full_name) -> None:
        self.park_code = park_code
        self.full_name = full_name
    
    description = None
    lat : float
    lon : float
    email : str
    phone : str
    entrance_fees : list
    entrance_passes : list
    operating_hours : dict


def park_data_collection(state,search_query,park_code=None,limit=5):
    url=base_url+"/parks"
    parks_data_list = []
    api_key = os.getenv('NPS_API_KEY')
    query = {"api_key":api_key, "q":search_query,"stateCode":state,"limit":limit,"parkCode":park_code}
    response = requests.get(url,params=query)
    response_data = response.json()[0]

    for park in response_data:
        new_park = Park(park.get("parkCode"),park.get("fullName"))
        new_park.description = park.get("description")
        new_park.lat = park.get("latitude")
        new_park.lon = park.get("longitude")
        new_park.phone = park.get("contacts")[0].get("phoneNumbers")[0].get("phoneNumber")
        new_park.email = park.get("contacts")[0].get("emailAddresses")[0].get("emailAddress")
        new_park.entrance_fees = park.get("entranceFees")
        new_park.entrance_passes = park.get("entrancePasses")
        

        
    
park_data_collection("WY",None)