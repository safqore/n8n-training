from weather import get_weather
import unittest
from unittest.mock import patch

class TestWeather(unittest.TestCase):

    @patch("weather.requests.get")
    def test_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"current": {"temp_c": 30.5, "temp_f": 86.9}}

        celsius, fahrenheit = get_weather("karachi")

        self.assertEqual(celsius, 30.5)
        self.assertEqual(fahrenheit, 86.9)

    @patch("weather.requests.get")
    def test_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        celsius, fahrenheit = get_weather("unknown")

        self.assertIsNone(celsius)
        self.assertIsNone(fahrenheit)   

if __name__ == "__main__":
    unittest.main()