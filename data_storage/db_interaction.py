import requests
import sqlite3
import os
from collections import OrderedDict
from .park import Park
db = 'bookmark.db'

class ParksDB:
    """
    A class that represents a collection of national parks.
    """


    instance = None

    class __Parks:
        """
        A private class that initializes the necessary tables in the database.
        """

        def __init__(self):
            """
            Initializes the database by creating three tables: NPS, Unsplash, and OpenWeather.
            """

            create_NPS_table = 'CREATE TABLE IF NOT EXISTS NPS (ParkCode TEXT PRIMARY KEY, ParkName TEXT, Latitude DECIMAL(3,8), Longitude DECIMAL(3,8), ParkDescription TEXT, StateCode TEXT, PhoneNum TEXT, Email TEXT)'

            create_Unsplash_table = 'CREATE TABLE IF NOT EXISTS Unsplash (ParkCode TEXT PRIMARY KEY, ImageURL TEXT, ImageDescription TEXT, Creator TEXT, CreatorURL TEXT)'

            create_OpenWeather_table = 'CREATE TABLE IF NOT EXISTS OpenWeather (ParkCode TEXT PRIMARY KEY, Day DATE, TimeOfDay DATETIME, Temperature DECIMAL(3,1), FeelsLike DECIMAL(3,1), WeatherDescription TEXT, WindSpeed DECIMAL(3,3), UNIQUE (Day, TimeOfDay))'

            conn = sqlite3.connect(db)

            with conn:
                conn.execute(create_NPS_table)
                conn.execute(create_Unsplash_table)
                conn.execute(create_OpenWeather_table)
            
            conn.commit()
            conn.close()

    def __init__(self):
        """
        Initializes the instance of the Parks class and creates an instance of the __Parks class if it doesn't already exist.
        """
        if not ParksDB.instance:
            ParksDB.instance = ParksDB.__Parks()

    def __getattr__(self, name):
        """
        Retrieves the attribute specified by the name parameter from the instance of the __Parks class.
        """
        return getattr(self.instance, name)
    
    def populate_nps_table(self, park):
        """
        Populates the NPS table in the database with the data of the specified park.

        Parameters:
        park (object): A national park object containing its relevant data.

        Returns:
        None
        """
        # SQL statement to insert park data
        insert_sql = '''INSERT INTO NPS
                        (ParkCode, ParkName, Latitude, Longitude, ParkDescription, StateCode, PhoneNum, Email)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

        # execute SQL statement with park data
        conn = sqlite3.connect(db)
        with conn:
            conn.execute(insert_sql, (park.park_code, park.name, park.latitude, park.longitude,
                                      park.description, park.state_code, park.phone, park.email))
        conn.commit()
        conn.close()
    
    def populate_unsplash_table(self, image_list):
        """
        Populates the Unsplash table in the database with the image data of the specified park.

        Parameters:
        None

        Returns:
        None
        """
        # call create_image_object to retrieve list of image objects
        images = create_image_object()
        
        # insert each image into Unsplash table
        conn = sqlite3.connect(db)
        with conn:
            for image in images:
                # SQL statement to insert image data
                insert_sql = '''INSERT INTO Unsplash
                                (ParkCode, ImageURL, ImageDescription, Creator, CreatorURL)
                                VALUES (?, ?, ?, ?, ?)'''

                # execute SQL statement with image data
                conn.execute(insert_sql, (self.park_code, image.image_url, image.description,
                                          image.creator_name, image.creator_link))
        conn.commit()
        conn.close()

    def populate_openweather_table(self,park):
        """
        Populates the OpenWeather table with forecast data for the park.

        Args:
        forecast_response (dict): A dictionary containing the forecast data for the park.

        Returns:
        None.
        """
        # call extract_data to retrieve dictionary of list of the forecast
        weather = park.forecast

        # insert each forecast record into OpenWeather table
        conn = sqlite3.connect(db)
        with conn:
            for day, forecast in weather.items():
                for time, values in forecast:
                    # SQL statement to insert forecast data
                    insert_sql = '''INSERT INTO OpenWeather
                                    (ParkCode, Day, TimeOfDay, Temperature, FeelsLike, WeatherDescription, WindSpeed)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)'''

                    # execute SQL statement with forecast data
                    conn.execute(insert_sql, (self.park_code, day, time, values[0], values[1], values[2], values[3]))
        conn.commit()
        conn.close()

    def get_all_park_info(self):
        """
        Retrieves information about a specific park from the NPS table.

        Parameters:
        park_code (str): The park code of the park to retrieve.

        Returns:
        A dictionary containing information about the park, including its name, location, description,
        phone number, and email.
        """
        select_sql = '''SELECT *
                         FROM NPS
                         '''

        conn = sqlite3.connect(db)
        with conn:
            results = conn.execute(select_sql).fetchall()
            if results:
                retrieved_park_list = []
                for result in results:
                    park_code = result[0]
                    park_name = result[1]
                    latitude = result[2]
                    longitude = result [3]
                    description = result[4]
                    state_code = result[5]
                    phone = result[6]
                    email = result[7]
                    retrieved_park = Park(park_name, description, state_code, latitude, longitude, park_code, phone, email)
                    retrieved_park_list.append(retrieved_park)
                return retrieved_park_list
            else:
                return None

    def get_park_info(self, park_code):
        """
        Retrieves information about a specific park from the NPS table.

        Parameters:
        park_code (str): The park code of the park to retrieve.

        Returns:
        A dictionary containing information about the park, including its name, location, description,
        phone number, and email.
        """
        select_sql = '''SELECT ParkName, Latitude, Longitude, ParkDescription, StateCode, PhoneNum, Email
                         FROM NPS
                         WHERE ParkCode = ?'''

        conn = sqlite3.connect(db)
        with conn:
            result = conn.execute(select_sql, (park_code,)).fetchone()

            if result:
                park_code = park_code
                park_name = result[0]
                latitude = result[1]
                longitude = result [2]
                description = result[3]
                state_code = result[4]
                phone = result[5]
                email = result[6]
                retrieved_park = Park(park_name, description, state_code, latitude, longitude, park_code, phone, email)
                return retrieved_park
            else:
                return None




    def get_park_image(self, park_code):
        """
        Retrieves an image of a specific park from the Unsplash table.

        Parameters:
        park_code (str): The park code of the park to retrieve the image for.

        Returns:
        A dictionary containing information about the image, including its URL, description, and creator information.
        """
        select_sql = '''SELECT ImageURL, ImageDescription, Creator, CreatorURL
                         FROM Unsplash
                         WHERE ParkCode = ?'''

        conn = sqlite3.connect(db)
        with conn:
            result = conn.execute(select_sql, (park_code,)).fetchone()

        if result:
            image_info = {
                'park_code': park_code,
                'image_url': result[0],
                'description': result[1],
                'creator_name': result[2],
                'creator_link': result[3]
            }
            return image_info
        else:
            return None



    def get_park_weather(self, park_code):
        """
        Retrieves weather information for a specific park from the OpenWeather table.

        Parameters:
        park_code (str): The park code of the park to retrieve the weather for.

        Returns:
        A list of dictionaries, with each dictionary representing a forecast for a specific day and time.
        Each dictionary contains the day, time, temperature, "feels like" temperature, weather description,
        and wind speed for the forecast.
        """
        select_sql = '''SELECT Day, TimeOfDay, Temperature, FeelsLike, WeatherDescription, WindSpeed
                         FROM OpenWeather
                         WHERE ParkCode = ?
                         ORDER BY Day, TimeOfDay'''

        conn = sqlite3.connect(db)
        with conn:
            results = conn.execute(select_sql, (park_code,)).fetchall()

            if results:
                forecast = OrderedDict()
                for item in forecast_response:
                    day_of_week = results[0]
                    if day_of_week not in forecast.keys():
                        # Extract data from the forecast response and store it in the dictionary
                        # using the day of the week for the key and the time of day for each 3 hour section.
                        # use a list for the specific data like temp

                        # 'park_code': park_code,
                        # 'day': result[0],
                        # 'time': result[1],
                        # 'temperature': result[2],
                        # 'feels_like': result[3],
                        # 'description': result[4],
                        # 'wind_speed': result[5]

                        forecast[day_of_week] = [[
                                                                results[1],
                                                                [
                                                                    results[2], 
                                                                    results[3],
                                                                    results[4],
                                                                    results[5]
                                                                ]
                                                            ]]  
                    else:                                                                       
                        forecast[day_of_week].append([
                                                            results[1],
                                                            [
                                                                results[2], 
                                                                results[3],
                                                                results[4],
                                                                results[5]
                                                            ],
                                                            ])
                return forecast
            else:
                return None

if __name__ == '__main__':
    ParksDB()