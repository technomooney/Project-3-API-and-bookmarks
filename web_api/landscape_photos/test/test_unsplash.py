import unittest
from unittest import TestCase
from unittest.mock import patch

import unsplash

class UnsplashTest(TestCase):

    @patch('unsplash.get_image_response')
    def test_get_image_response(self, mock_response):
        """"""