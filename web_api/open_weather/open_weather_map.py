import requests
import os
from datetime import datetime
from pprint import pprint
from collections import OrderedDict
# Configure logging
# logging.basicConfig(filename='weather.log', level=logging.INFO)

""" functions for getting weather for a specific latitude and longitude and extract the data in a useful 5 day format """


# Read API key from environment variable
api_key = os.environ['WEATHER_KEY']

def get_api_response(lat,lon,url='https://api.openweathermap.org/data/2.5/forecast'):
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


def extract_data(forecast_response):

    """
    forecast data is in the following format for the forecast attribute of the park object that was passed.
    {'Tuesday':[[15:00:00, [temp, feels_like temp, weather desc, wind speed], dt], [...], [...]]
    'Wednesday':[[12:00:00, [temp, feels_like temp, weather desc, wind speed], dt], [...], [...]],... etc}
    """
    try:
        # Loop over forecast data and add data to the weather object
        forecast = OrderedDict()
        
        for item in forecast_response:
            date_time = datetime.fromtimestamp(item['dt']) # convert the unix timestamp to a datetime object
            day_of_week = date_time.strftime("%A") # get the day that this specific entry is on
            if day_of_week not in forecast.keys():
                # Extract data from the forecast response and store it in the dictionary
                # using the day of the week for the key and the time of day for each 3 hour section.
                # use a list for the specific data like temp
                forecast[day_of_week] = [[
                                                        date_time.strftime("%X"),
                                                        [
                                                            item['main']['temp'], 
                                                            item['main']['feels_like'],
                                                            item['weather'][0]['description'],
                                                            item['wind']['speed']
                                                        ],
                                                        item['dt']
                                                    ]]  
            else:                                                                       
                forecast[day_of_week].append([
                                                    date_time.strftime("%X"),
                                                    [
                                                        item['main']['temp'], 
                                                        item['main']['feels_like'],
                                                        item['weather'][0]['description'],
                                                        item['wind']['speed']
                                                    ],
                                                    item['dt']])
        return forecast
    except ValueError as val_err:
        return val_err
    except Exception as err:
        return err
if __name__ == '__main__':
    forecast_response, error = get_api_response(lat = 44.59824417, lon = -110.5471695)
    print(error)
    forecast = extract_data(forecast_response)
    pprint(forecast)
    print(forecast)
