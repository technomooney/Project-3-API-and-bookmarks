import unittest
from unittest.mock import patch

# import classes and functions
from national_parks import Park, search_parks, select_park

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
    @patch('national_parks.requests.get')
    def test_search_parks(self, mock_get):
        
        # A mock response object with a list of parks
        mock_response = {'data': [{'fullName': 'Yellowstone National Park', 'description': 'A national park located in Wyoming', 'states': 'WY', 'latLong': '44.59824417, -110.5471694', 'parkCode': 'yell', 'contacts': {'phoneNumbers': [{'phoneNumber': '307-344-7381'}], 'emailAddresses': [{'emailAddress': 'yellowstone@nps.gov'}]} }]}
        
        # The return value of the mock response 
        mock_get.return_value.json.return_value = mock_response

        # Call the search_parks function with a search term
        parks = search_parks('Yellowstone')

        # Test that the function returns the correct number of parks and the correct park
        self.assertEqual(len(parks), 1)
        self.assertEqual(parks[0].name, 'Yellowstone National Park')

# A test case for the select park function
class TestSelectPark(unittest.TestCase):
    # A setup method that creates a list of parks to use in test
    def setUp(self):
        self.parks = [
             Park('Yellowstone National Park', 'A national park located in Wyoming', 'WY', '44.59824417, -110.5471694', 'yell', '307-344-7381', 'yellowstone@nps.gov'),
            Park('Yosemite National Park', 'A national park located in California', 'CA', '37.86510176, -119.5383301', 'yose', '209-372-0200', 'yose@nps.gov'),
            Park('Grand Canyon National Park', 'A national park located in Arizona', 'AZ', '36.1069625, -112.112552', 'grca', '928-638-7888', 'grca@nps.gov')
        ]
    
    # The patch decorator mocks the input function so that it returns 1 when called.
    @patch('builtins.input', side_effect=['1'])
    def test_select_park(self, mock_input):
        selected_park = select_park(self.parks)
        self.assertEqual(selected_park.name, 'Yellowstone National Park') # Checks the name attribute of the selected park.

    # Test whether the function correctly handles invalid input.
    @patch('builtins.input', side_effects=['5', '1'])  # The patch mocks the input function so that it returns 5 
    def test_select_park_invalid_input(self, mock_input):
        selected_park = select_park(self.parks)
        self.assertEqual(selected_park.name, 'Yellowstone National Park') #  Checks the name attribute of the selected park.

if __name__ == '__main__':
    unittest.main()


# Documentation | Resources
"""
https://docs.python.org/3/library/unittest.mock.html
https://ralphmcneal.com/unit-testing-with-pythons-patch-decorator/

https://stackoverflow.com/questions/15753390/how-can-i-mock-requests-and-the-response



"""