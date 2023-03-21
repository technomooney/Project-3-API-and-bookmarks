import unittest
import sqlite3

# Setting the name of the database file
db = 'bookmark.db'

# Defining a unit test class for testing the bookmark database
class TestParksDatabase(unittest.TestCase):

    # Creating a setUp method to run before each test method
    def setUp(self):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    # Creating a method to clear out the test data once the tests are done
    def clear_tables(self):
        with self.conn:
            self.cursor.execute("DELETE FROM NPS")
            self.cursor.execute("DELETE FROM Unsplash")
            self.cursor.execute("DELETE FROM OpenWeather")
            self.conn.commit()

    # Creating a teardown method to run after each test method
    def tearDown(self):
        self.clear_tables()
        self.conn.close()

    # This tests that the database has been created and all tables expected exist
    def test_database_creation(self):
        # Check if the database is created
        self.assertIsNotNone(self.conn)
    
        # Check if NPS table exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='NPS'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
    
        # Check if Unsplash table exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Unsplash'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
    
        # Check if OpenWeather table exists
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='OpenWeather'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    # This tests that all columns are setup correctly for the data expected for the NPS table
    def test_NPS_table_columns(self):
        self.cursor.execute("PRAGMA table_info(NPS)")
        columns = self.cursor.fetchall()
        expected_columns = [
            (0, 'ParkCode', 'INTEGER', 0, None, 1),
            (1, 'ParkName', 'TEXT', 0, None, 0),
            (2, 'Latitude', 'DECIMAL(3,8)', 0, None, 0),
            (3, 'Longitude', 'DECIMAL(3,8)', 0, None, 0),
            (4, 'ParkDescription', 'TEXT', 0, None, 0),
            (5, 'PhoneNum', 'TEXT', 0, None, 0),
            (6, 'Email', 'TEXT', 0, None, 0)
        ]
        self.assertEqual(columns, expected_columns)

    # This tests that all columns are setup correctly for the data expected for the Unsplash table
    def test_Unsplash_table_columns(self):
        self.cursor.execute("PRAGMA table_info(Unsplash)")
        columns = self.cursor.fetchall()
        expected_columns = [
            (0, 'ParkCode', 'INTEGER', 0, None, 1),
            (1, 'ImageURL', 'TEXT', 0, None, 0),
            (2, 'ImageDescription', 'TEXT', 0, None, 0),
            (3, 'Creator', 'TEXT', 0, None, 0),
            (4, 'CreatorURL', 'TEXT', 0, None, 0)
        ]
        self.assertEqual(columns, expected_columns)

    # This tests that all columns are setup correctly for the data expected for the OpenWeather table
    def test_OpenWeather_table_columns(self):
        self.cursor.execute("PRAGMA table_info(OpenWeather)")
        columns = self.cursor.fetchall()
        expected_columns = [
            (0, 'ParkCode', 'INTEGER', 0, None, 1),
            (1, 'Day', 'DATE', 0, None, 0),
            (2, 'TimeOfDay', 'DATETIME', 0, None, 0),
            (3, 'Temperature', 'DECIMAL(3,1)', 0, None, 0),
            (4, 'FeelsLike', 'DECIMAL(3,1)', 0, None, 0),
            (5, 'WeatherDescription', 'TEXT', 0, None, 0),
            (6, 'WindSpeed', 'DECIMAL(3,3)', 0, None, 0)
        ]
        self.assertEqual(columns, expected_columns)

    # This tests all three tables to make sure data can be inserted into them correctly
    def test_insert_new_row_updates_info(self):
        # Insert a new park into the NPS table
        park_code = 12345
        park_name = "New Park"
        latitude = 37.7749
        longitude = -122.4194
        park_description = "A beautiful new park"
        phone_num = "555-555-5555"
        email = "newpark@example.com"
        self.cursor.execute("INSERT INTO NPS (ParkCode, ParkName, Latitude, Longitude, ParkDescription, PhoneNum, Email) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (park_code, park_name, latitude, longitude, park_description, phone_num, email))
        self.conn.commit()

        # Check that the park's information was updated correctly in NPS table
        result = self.cursor.execute("SELECT * FROM NPS WHERE ParkCode = ?", (park_code,)).fetchone()
        self.assertEqual(result[0], park_code)
        self.assertEqual(result[1], park_name)
        self.assertEqual(result[2], latitude)
        self.assertEqual(result[3], longitude)
        self.assertEqual(result[4], park_description)
        self.assertEqual(result[5], phone_num)
        self.assertEqual(result[6], email)

        # Insert a new image into the Unsplash table
        park_code = 12345
        image_url = "https://unsplash.com/photos/xxxxxx"
        image_description = "Beautiful scenery"
        creator = "John Doe"
        creator_url = "https://unsplash.com/@johndoe"
        self.cursor.execute("INSERT INTO Unsplash (ParkCode, ImageURL, ImageDescription, Creator, CreatorURL) VALUES (?, ?, ?, ?, ?)",
                            (park_code, image_url, image_description, creator, creator_url))
        self.conn.commit()

        # Check that the park's information was updated correctly in Unsplash table
        result = self.cursor.execute("SELECT * FROM Unsplash WHERE ParkCode = ?", (park_code,)).fetchone()
        self.assertEqual(result[0], park_code)
        self.assertEqual(result[1], image_url)
        self.assertEqual(result[2], image_description)
        self.assertEqual(result[3], creator)
        self.assertEqual(result[4], creator_url)

        # Insert a new weather data into the OpenWeather table
        park_code = 12345
        day = "2022-01-01"
        time_of_day = "12:00:00"
        temperature = 50.5
        feels_like = 47.2
        weather_description = "Sunny"
        wind_speed = 3.2
        self.cursor.execute("INSERT INTO OpenWeather (ParkCode, Day, TimeOfDay, Temperature, FeelsLike, WeatherDescription, WindSpeed) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (park_code, day, time_of_day, temperature, feels_like, weather_description, wind_speed))
        self.conn.commit()

        # Check that the park's information was updated correctly in OpenWeather table
        result = self.cursor.execute("SELECT * FROM OpenWeather WHERE ParkCode = ? AND Day = ? AND TimeOfDay = ?", (park_code, day, time_of_day)).fetchone()
        self.assertEqual(result[0], park_code)
        self.assertEqual(result[1], day)
        self.assertEqual(result[2], time_of_day)
        self.assertEqual(result[3], temperature)
        self.assertEqual(result[4], feels_like)
        self.assertEqual(result[5], weather_description)
        self.assertEqual(result[6], wind_speed)

    # This tests that no duplicates can be entered into the database
    # def test_no_duplicate_rows(self):
    #     # Insert a row with a unique ParkCode
    #     self.cursor.execute("INSERT INTO NPS (ParkCode, ParkName, Latitude, Longitude, ParkDescription, PhoneNum, Email) VALUES (1, 'Yellowstone', 44.6, -110.5, 'First national park', '555-555-5555', 'example@example.com')")
    #     self.conn.commit()
    
    #     # Attempt to insert a row with the same ParkCode
    #     with self.assertRaises(sqlite3.IntegrityError):
    #         self.cursor.execute("INSERT INTO NPS (ParkCode, ParkName, Latitude, Longitude, ParkDescription, PhoneNum, Email) VALUES (1, 'Duplicate Park', 0, 0, 'This row should not be inserted', '555-555-5555', 'example@example.com')")
    #         self.conn.commit()
        
    #     # Attempt to insert a row with the same ParkCode into Unsplash
    #     with self.assertRaises(sqlite3.IntegrityError):
    #         self.cursor.execute("INSERT INTO Unsplash (ParkCode, ImageURL, ImageDescription, Creator, CreatorURL) VALUES (1, 'https://example.com/image.jpg', 'This row should not be inserted', 'John Doe', 'https://example.com/creator')")
    #         self.conn.commit()
        
    #     # Attempt to insert a row with the same ParkCode into OpenWeather
    #     with self.assertRaises(sqlite3.IntegrityError):
    #         self.cursor.execute("INSERT INTO OpenWeather (ParkCode, Day, TimeOfDay, Temperature, FeelsLike, WeatherDescription, WindSpeed) VALUES (1, '2022-01-01', '2022-01-01 12:00:00', 32.0, 25.0, 'Sunny', 5.0)")
    #         self.conn.commit()

if __name__ == '__main__':
    unittest.main()