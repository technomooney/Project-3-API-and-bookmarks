import requests
import os
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='weather.log', level=logging.INFO)

# Read API key from environment variable
api_key = os.environ['OPENWEATHERMAP_API_KEY']
url = 'https://api.openweathermap.org/data/2.5/forecast'

# Prompt user for location
location = input('Enter a city name: ')

# Set query parameters for API request
params = {'q': location, 'units': 'metric', 'appid': api_key}

# Send API request and handle errors
try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    logging.error(f'API request failed: {e}')
    print('Sorry, there was an error getting the weather forecast.')
    exit()

# Extract forecast data from response and handle missing data
forecast = response.json().get('list', [])
if not forecast:
    logging.warning('No forecast data found for location: %s', location)
    print('Sorry, we could not find any weather forecast data for that location.')
    exit()

# Set timezone offset for Minnesota
mn_tz_offset = -6

# Loop over forecast data and display information
for data in forecast:
    # Extract timestamp from data
    timestamp_str = data['dt_txt']

    # Convert timestamp string to datetime object (UTC time)
    timestamp_utc = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')

    # Calculate local time in Minnesota using timezone offset
    timestamp_mn = timestamp_utc + timedelta(hours=mn_tz_offset)

    # Extract temperature and wind speed from data
    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']

    # Format output string with local time and weather information
    output_str = f'{timestamp_mn}: {temperature} C - {data["weather"][0]["description"]}, Wind speed: {wind_speed} m/s'

    # Log output string
    logging.info(output_str)

    # Print output string
    print(output_str)
