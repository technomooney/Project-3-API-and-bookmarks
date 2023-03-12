import unittest
from api import park_data_collection

# In this test module, we import the api.py module and the Park class to test the park_data_collection function.
from api import park_data_collection

class TestApi(unittest.TestCase):

# We test the function by calling it with different parameters.
    def test_park_data_collection(self):
        # Test with state = "ca", search_query = "", park_code = None, limit = 5

        parks = park_data_collection("ca")
        self.assertEqual(len(parks), 5)
        self.assertEqual(parks[0].__class__.__name__, "Park")
        self.assertIsNotNone(parks[0].full_name)
        self.assertIsNotNone(parks[0].park_code)
        self.assertIsNotNone(parks[0].lat)
        self.assertIsNotNone(parks[0].lon)
        self.assertIsNotNone(parks[0].phone)
        self.assertIsNotNone(parks[0].email)
        self.assertIsNotNone(parks[0].entrance_fees)
        self.assertIsNotNone(parks[0].entrance_passes)
        self.assertIsNotNone(parks[0].operating_hours)
        
        # Test with state  = "co", search_query = "canyon, park_code = None, limit = 10 "
        # We also test that each park object in the list has all its attributes populated with

        parks = park_data_collection("co", "canyon", None, 10)
        self.assertEqual(len(parks), 10)
        self.assertEqual(parks[0].__class__.__name__, "Park")
        self.assertIsNotNone(parks[0].full_name)
        self.assertIsNotNone(parks[0].park_code)
        self.assertIsNotNone(parks[0].lat)
        self.assertIsNotNone(parks[0].lon)
        self.assertIsNotNone(parks[0].phone)
        self.assertIsNotNone(parks[0].email)
        self.assertIsNotNone(parks[0].entrance_fees)
        self.assertIsNotNone(parks[0].entrance_passes)
        self.assertIsNotNone(parks[0].operating_hours)

# We use unittest.main() to run the tests when we run the module directly.
if __name__ == '__main__':
    unittest.main()        