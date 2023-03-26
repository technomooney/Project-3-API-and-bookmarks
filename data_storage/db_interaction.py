import requests
import sqlite3
import os

db = 'bookmark.db'

class ParksDB:
    """A class that represents a collection of national parks."""

    instance = None

    class __Parks:
        """A private class that initializes the necessary tables in the database."""

        def __init__(self):
            """Initializes the database by creating three tables: NPS, Unsplash, and OpenWeather."""

            create_NPS_table = 'CREATE TABLE IF NOT EXISTS NPS (ParkCode INTEGER PRIMARY KEY, ParkName TEXT, Latitude DECIMAL(3,8), Longitude DECIMAL(3,8), ParkDescription TEXT, PhoneNum TEXT, Email TEXT)'

            create_Unsplash_table = 'CREATE TABLE IF NOT EXISTS Unsplash (ParkCode INTEGER PRIMARY KEY, ImageURL TEXT, ImageDescription TEXT, Creator TEXT, CreatorURL TEXT)'

            create_OpenWeather_table = 'CREATE TABLE IF NOT EXISTS OpenWeather (ParkCode INTEGER PRIMARY KEY, Day DATE, TimeOfDay DATETIME, Temperature DECIMAL(3,1), FeelsLike DECIMAL(3,1), WeatherDescription TEXT, WindSpeed DECIMAL(3,3), UNIQUE (Day, TimeOfDay))'

            conn = sqlite3.connect(db)

            with conn:
                conn.execute(create_NPS_table)
                conn.execute(create_Unsplash_table)
                conn.execute(create_OpenWeather_table)
            
            conn.commit()
            conn.close()

    def __init__(self):
        """Initializes the instance of the Parks class and creates an instance of the __Parks class if it doesn't already exist."""

        if not ParksDB.instance:
            ParksDB.instance = ParksDB.__Parks()

    def __getattr__(self, name):
        """Retrieves the attribute specified by the name parameter from the instance of the __Parks class."""

        return getattr(self.instance, name)
    
    def populate_nps_table(self, park):
        """Populates the NPS table in the database with the data of the specified park.

        Parameters:
        park (object): A national park object containing its relevant data.

        Returns:
        None"""

        # SQL statement to insert park data
        insert_sql = '''INSERT INTO NPS
                        (ParkCode, ParkName, Latitude, Longitude, ParkDescription, PhoneNum, Email)
                        VALUES (?, ?, ?, ?, ?, ?, ?)'''

        # execute SQL statement with park data
        conn = sqlite3.connect(db)
        with conn:
            conn.execute(insert_sql, (park.park_code, park.name, park.location[0], park.location[1],
                                      park.description, park.phone, park.email))
        conn.commit()
        conn.close()
    
    def populate_unsplash_table(self):
        """Populates the Unsplash table in the database with the image data of the specified park.

        Parameters:
        None

        Returns:
        None"""

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

    def populate_openweather_table(self):
        """Populates the OpenWeather table with forecast data for the park.

        Args:
        forecast_response (dict): A dictionary containing the forecast data for the park.

        Returns:
        None."""
        
        # call extract_data to retrieve dictionary of list of the forecast
        weather = extract_data(self, forecast_response)

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


    
if __name__ == '__main__':
    ParksDB()