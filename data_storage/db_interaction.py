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
    
if __name__ == '__main__':
    Parks()