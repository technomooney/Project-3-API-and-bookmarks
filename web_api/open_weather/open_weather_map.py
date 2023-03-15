import requests
import os
from datetime import datetime, timedelta

class weather_data():
    def __init__(self,park_code:str, location:str) -> None:
        self.park_code = park_code
        self.location = location
        weather_info_list: list


    

# Configure logging
# logging.basicConfig(filename='weather.log', level=logging.INFO)

# Read API key from environment variable
api_key = os.environ['OPENWEATHERMAP_API_KEY']
url = 'https://api.openweathermap.org/data/2.5/forecast'

def get_api_response(url,lat,lon):
    # Set query parameters for API request
    params = {'lat':lat,'lon':lon, 'units': 'imperial', 'appid': api_key}

    # Send API request and handle errors, return data
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_json = response.json()['list']
        return response_json,None
    except requests.exceptions.RequestException as e:
        error = (f'API request failed: {e.response}',e)
        return None,error

        
def extract_data(weather_object,forecast_response):
    # Loop over forecast data and add data to the weather object
    for data in forecast_response:
        # Extract temperature and wind speed from data
        weather_object.temp = data['main']['temp']
        wind_speed = data['wind']['speed']
