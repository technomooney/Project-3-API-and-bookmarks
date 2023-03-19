import unittest
from unittest.mock import patch, Mock
import open_weather_map
import test_data.mock_data as mock_data
from parkweather import ParkWeather
import os

class TestPark():
            def __init__(self):
                self.lat = 44.59824417
                self.lon = -110.5471695
                self.park_code = "yell"

class TestAPIProcessing(unittest.TestCase):

    def test_extract_data_valid_json(self):
        forecast_response = mock_data.mock_extracted_forecast_json
        park_object = ParkWeather("yell")
        expected={'Friday': [{'15:00:00': [14.47, 7.29, 'scattered clouds', 4.38]}, {'18:00:00': [18.55, 13.19, 'few clouds', 3.56]}, {'21:00:00': [1.92, 1.92, 'clear sky', 0.81]}], 'Saturday': [{'00:00:00': [-4.79, -4.79, 'clear sky', 2.73]}, {'03:00:00': [-7.8, -16.33, 'broken clouds', 3.27]}, {'06:00:00': [-8.7, -16.94, 'broken clouds', 3.09]}, {'09:00:00': [6.91, 0.57, 'scattered clouds', 3.18]}, {'12:00:00': [23.65, 17.6, 'few clouds', 4.7]}, {'15:00:00': [27.82, 18.64, 'clear sky', 9.84]}, {'18:00:00': [24.57, 16.23, 'few clouds', 7.4]}, {'21:00:00': [9.01, 9.01, 'overcast clouds', 2.59]}], 'Sunday': [{'00:00:00': [1.17, -6, 'broken clouds', 3.2]}, {'03:00:00': [-2.09, -11.27, 'broken clouds', 3.98]}, {'06:00:00': [-3.28, -12.73, 'broken clouds', 4.03]}, {'09:00:00': [8.29, 1.09, 'broken clouds', 3.76]}, {'12:00:00': [24.66, 16.93, 'scattered clouds', 6.64]}, {'15:00:00': [28.54, 19.69, 'scattered clouds', 9.55]}, {'18:00:00': [27.32, 20.7, 'broken clouds', 5.95]}, {'21:00:00': [13.55, 7.57, 'overcast clouds', 3.49]}], 'Monday': [{'00:00:00': [12.42, 6.31, 'overcast clouds', 3.47]}, {'03:00:00': [9.91, 3.54, 'overcast clouds', 3.42]}, {'06:00:00': [11.8, 11.8, 'overcast clouds', 2.68]}, {'09:00:00': [19.27, 13.71, 'light snow', 3.76]}, {'12:00:00': [27.07, 19.4, 'light snow', 7.2]}, {'15:00:00': [30.29, 22.57, 'light snow', 8.32]}, {'18:00:00': [29.48, 23.88, 'light snow', 5.26]}, {'21:00:00': [20.01, 20.01, 'overcast clouds', 0.96]}], 'Tuesday': [{'00:00:00': [21.31, 21.31, 'light snow', 2.04]}, {'03:00:00': [22.41, 22.41, 'light snow', 2.68]}, {'06:00:00': [22.41, 14.61, 'snow', 6.22]}, {'09:00:00': [19.69, 9.25, 'light snow', 8.84]}, {'12:00:00': [22.35, 10, 'light snow', 13.29]}, {'15:00:00': [24.8, 13.03, 'light snow', 13.49]}, {'18:00:00': [22.33, 12.58, 'overcast clouds', 8.7]}, {'21:00:00': [12.78, 12.78, 'overcast clouds', 2.26]}], 'Wednesday': [{'00:00:00': [8.49, 8.49, 'overcast clouds', 2.19]}, {'03:00:00': [2.62, 2.62, 'broken clouds', 2.71]}, {'06:00:00': [-0.27, -0.27, 'broken clouds', 2.93]}, {'09:00:00': [11.59, 11.59, 'broken clouds', 2.21]}, {'12:00:00': [25.02, 25.02, 'scattered clouds', 2.66]}]}
        open_weather_map.extract_data(park_object, forecast_response)
        self.assertEquals(park_object.forecast, expected)

    def test_extract_data_unexpected_json(self):
        forecast_response = mock_data.mock_unexpected_extracted_forecast_data
        park_object = ParkWeather('yell')
        error = open_weather_map.extract_data(park_object, forecast_response)
        self.assertDictEqual({},park_object.forecast)


class TestAPIRequest(unittest.TestCase):
    
    @patch("requests.get")
    def test_return_list_from_requests(self,mock_get):
        mock_response = Mock()
        mock_response.json.return_value = mock_data.mock_get_api_response
        mock_get.json.return_value = mock_response
        test_park_object = TestPark()
        response = open_weather_map.get_api_response(test_park_object)
        self.assertListEqual(mock_data.mock_extracted_forecast_json, response)
        

if __name__ == '__main__':
    unittest.main()


