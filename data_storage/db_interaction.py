import sqlite3

db = 'bookmark.db'

class Parks:

    instance = None

    class __Parks:

        def __init__(self):

            create_NPS_table = 'CREATE TABLE IF NOT EXISTS NPS (ParkCode INTEGER PRIMARY KEY, ParkName TEXT, Latitude DECIMAL(3,8), Longitude DECIMAL(3,8), Description TEXT, PhoneNum TEXT, Email TEXT)'

            create_Unsplash_table = 'CREATE TABLE IF NOT EXISTS Unsplash (ParkCode INTEGER PRIMARY KEY, ImageURL TEXT, Description TEXT, Creator TEXT, CreatorURL TEXT)'

            create_OpenWeather_table = 'CREATE TABLE IF NOT EXISTS OpenWeather (ParkCode INTEGER PRIMARY KEY, Day DATE, TimeOfDay DATETIME, Temperature DECIMAL(3,1), FeelsLike DECIMAL(3,1), Description TEXT, WindSpeed DECIMAL(3,3), UNIQUE (Day, TimeOfDay))'

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
    
if __name__ == '__main__':
    Parks()