from unittest import TestCase
from unittest.mock import patch

import unsplash
import test_data.mock_unsplash_data as mock_unsplash_data
import test_data.mock_expected_results as mock_expected_results


class TestUnsplash(TestCase):

    @patch('requests.get')
    def test_get_image_response_narrowed_results(self, mock_response):
        
        example_api_response = mock_unsplash_data.mock_response
        mock_response().json.return_value = example_api_response

        expected_narrowed_results = mock_expected_results.mock_expected_narrowed_results
        results, error = unsplash.get_image_response()

        self.assertEqual(expected_narrowed_results, results)
    

    @patch('requests.get')
    def test_get_image_response_returns_10_images(self, mock_response):
        
        example_api_results = mock_expected_results.mock_expected_narrowed_results
        mock_response().json.return_value = example_api_results

        expected_number_results = 10
        number_results = len(example_api_results)

        self.assertEqual(expected_number_results, number_results)


    def test_create_image_object_list_returns_10_items(self):
        
        example_api_results = mock_expected_results.mock_expected_narrowed_results
        image_object_list = unsplash.create_image_object_list(example_api_results)

        expected_number_image_objects = 10
        number_image_objects = len(image_object_list)

        self.assertEqual(expected_number_image_objects, number_image_objects)     