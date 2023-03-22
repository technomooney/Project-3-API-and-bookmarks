import requests
import sqlite3
import os
from image import Image

db = 'bookmark.db'

class Parks:

    instance = None

    class __Parks:

        def __init__(self):

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
        if not Parks.instance:
            Parks.instance = Parks.__Parks()

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def populate_nps_table(self, park):
        # SQL statement to insert park data
        insert_sql = '''INSERT INTO NPS
                        (ParkCode, ParkName, Latitude, Longitude, ParkDescription, PhoneNum, Email)
                        VALUES (?, ?, ?, ?, ?, ?, ?)'''

        # execute SQL statement with park data
        conn = sqlite3.connect(db)
        with conn:
            conn.execute(insert_sql, (self.park_code, park.full_name, park.location[0], park.location[1],
                                      park.description, None, None))
        conn.commit()
        conn.close()
    
    def populate_unsplash_table(self):
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
    Parks()