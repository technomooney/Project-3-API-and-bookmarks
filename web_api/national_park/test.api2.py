import unittest
from unittest.mock import patch, Mock
from api import park_data_collection

class TestAPIFunctions(unittest.TestCase):

# this test case uses the @patch with a mock object that returns a predefined JSON response.

    @patch('api.request.get')
    def test_park_data_collection(self, mock_get):
        # Mock response from the API

        mock_response = Mock()
        mock_response.json.return_value = {
            "data": [
                {
                    "parkCode": "abcd",
                    "fullName": "Test Park",
                    "description": "This is a test park.",
                    "latitude": 42.1234,
                    "longitude": -71.5678,
                    "contacts": [
                        {
                            "phoneNumbers": [
                                {
                                    "phoneNumber": "555-1234"
                                }
                            ],
                            "emailAddresses": [
                                {
                                    "emailAddress": "test@example.com"
                                }
                            ]
                        }
                    ],
                    "entranceFees": [],
                    "entrancePasses": [],
                    "operatingHours": []
                }
            ]
        }
        mock_get.return_value = mock_response

        # Call the function with the mock response
        parks_data_list = park_data_collection("MA", park_code="abcd", limit=1)

        # check that the function returns the expected result 
        self.assertEqual(len(parks_data_list), 1)
        park = parks_data_list[0]
        self.assertEqual(park.park_code, "abcd")
        self.assertEqual(park.full_name, "Test Park")
        self.assertEqual(park.description, "This is a test park.")
        self.assertEqual(park.lat, 42.1234)
        self.assertEqual(park.lon, -71.5678)
        self.assertEqual(park.phone, "555-1234")
        self.assertEqual(park.email, "test@example.com")
        self.assertEqual(park.entrance_fees, [])
        self.assertEqual(park.entrance_passes, [])
        self.assertEqual(park.operating_hours, [])
        