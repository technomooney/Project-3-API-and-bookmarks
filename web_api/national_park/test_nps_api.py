import unittest
from unittest.mock import patch

# import classes and functions
from national_parks import Park, search_parks, select_parks

# A test case for the Park class
class TestPark(unittest.TestCase):
    # test the initialization of a park with some attributes
    def test_park_attributes(self):
        park = Park('Yellowstone National Park', 'A national park located in Wyoming', 'WY', '44.59824417, -110.5471694', 'yell', '307-344-7381', 'yellowstone@nps.gov')
        self.assertEqual(park.name, 'Yellowstone National Park')
        self.assertEqual(park.description, 'A national park located in Wyoming')
        self.assertEqual(park.state_code, 'WY')
        self.assertEqual(park.location, '44.59824417, -110.5471694')
        self.assertEqual(park.park_code, 'yell')
        self.assertEqual(park.phone, '307-344-7381')
        self.assertEqual(park.email, 'yellowstone@nps.gov')

# A test case for the search_parks function
class TestSearchParks(unittest.TestCase):
    # test the search_parks function with a mock response 
