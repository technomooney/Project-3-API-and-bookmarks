import unittest
from unittest.mock import patch, Mock
import open_weather_map
import test_data.mock_data as mock_data
from collections import OrderedDict
from pprint import pprint

class TestPark():
            def __init__(self):
                self.lat = 44.59824417
                self.lon = -110.5471695
                self.park_code = "yell"

class TestAPIProcessing(unittest.TestCase):

    def test_extract_data_valid_json(self):
        forecast_response = mock_data.mock_extracted_forecast_json
        expected=OrderedDict({'Friday': [['15:00:00', [9.68, 1.71, 'scattered clouds', 4.38], 1679086800], ['18:00:00', [16.14, 10.44, 'few clouds', 3.56], 1679097600], ['21:00:00', [1.92, 1.92, 'clear sky', 0.81], 1679108400]], 'Saturday': [['00:00:00', [-4.79, -4.79, 'clear sky', 2.73], 1679119200], ['03:00:00', [-7.8, -16.33, 'broken clouds', 3.27], 1679130000], ['06:00:00', [-8.7, -16.94, 'broken clouds', 3.09], 1679140800], ['09:00:00', [6.91, 0.57, 'scattered clouds', 3.18], 1679151600], ['12:00:00', [23.65, 17.6, 'few clouds', 4.7], 1679162400], ['15:00:00', [27.82, 18.64, 'clear sky', 9.84], 1679173200], ['18:00:00', [24.57, 16.23, 'few clouds', 7.4], 1679184000], ['21:00:00', [9.01, 9.01, 'overcast clouds', 2.59], 1679194800]], 'Sunday': [['00:00:00', [1.17, -6, 'broken clouds', 3.2], 1679205600], ['03:00:00', [-2.09, -11.27, 'broken clouds', 3.98], 1679216400], ['06:00:00', [-3.28, -12.73, 'broken clouds', 4.03], 1679227200], ['09:00:00', [8.29, 1.09, 'broken clouds', 3.76], 1679238000], ['12:00:00', [24.66, 16.93, 'scattered clouds', 6.64], 1679248800], ['15:00:00', [28.54, 19.69, 'scattered clouds', 9.55], 1679259600], ['18:00:00', [27.32, 20.7, 'broken clouds', 5.95], 1679270400], ['21:00:00', [13.55, 7.57, 'overcast clouds', 3.49], 1679281200]], 'Monday': [['00:00:00', [12.42, 6.31, 'overcast clouds', 3.47], 1679292000], ['03:00:00', [9.91, 3.54, 'overcast clouds', 3.42], 1679302800], ['06:00:00', [11.8, 11.8, 'overcast clouds', 2.68], 1679313600], ['09:00:00', [19.27, 13.71, 'light snow', 3.76], 1679324400], ['12:00:00', [27.07, 19.4, 'light snow', 7.2], 1679335200], ['15:00:00', [30.29, 22.57, 'light snow', 8.32], 1679346000], ['18:00:00', [29.48, 23.88, 'light snow', 5.26], 1679356800], ['21:00:00', [20.01, 20.01, 'overcast clouds', 0.96], 1679367600]], 'Tuesday': [['00:00:00', [21.31, 21.31, 'light snow', 2.04], 1679378400], ['03:00:00', [22.41, 22.41, 'light snow', 2.68], 1679389200], ['06:00:00', [22.41, 14.61, 'snow', 6.22], 1679400000], ['09:00:00', [19.69, 9.25, 'light snow', 8.84], 1679410800], ['12:00:00', [22.35, 10, 'light snow', 13.29], 1679421600], ['15:00:00', [24.8, 13.03, 'light snow', 13.49], 1679432400], ['18:00:00', [22.33, 12.58, 'overcast clouds', 8.7], 1679443200], ['21:00:00', [12.78, 12.78, 'overcast clouds', 2.26], 1679454000]], 'Wednesday': [['00:00:00', [8.49, 8.49, 'overcast clouds', 2.19], 1679464800], ['03:00:00', [2.62, 2.62, 'broken clouds', 2.71], 1679475600], ['06:00:00', [-0.27, -0.27, 'broken clouds', 2.93], 1679486400], ['09:00:00', [11.59, 11.59, 'broken clouds', 2.21], 1679497200], ['12:00:00', [25.02, 25.02, 'scattered clouds', 2.66], 1679508000]]})
        forecast_dict = open_weather_map.extract_data(forecast_response)
        self.assertEqual(expected,forecast_dict)

    def test_extract_data_unexpected_json(self):
        forecast_response = mock_data.mock_unexpected_extracted_forecast_data
        forecast = open_weather_map.extract_data(forecast_response)
        self.assertDictEqual({},forecast)


class TestAPIRequest(unittest.TestCase):
    
    @patch("requests.Response.json")
    def test_return_list_from_requests(self,mock_json):
        mock_json.return_value = mock_data.mock_json_api_response
        response,err = open_weather_map.get_api_response(lon = -110.5471695,lat = 44.59824417)
        self.assertListEqual(mock_data.mock_extracted_forecast_json, response)
        

if __name__ == '__main__':
    unittest.main()


