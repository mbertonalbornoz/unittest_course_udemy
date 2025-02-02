import unittest
from unittest.mock import MagicMock, patch

from advanced_mocking.my_module import get_weather


# Enter your solution here
class TestGetWeather(unittest.TestCase):
    @patch('requests.get')
    def test_success(self, get_mock):
        # GIVEN
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value ={
                "name": 'Bahia Blanca',
                "main": {
                    "temp": 38,
                    "humidity": 0.86
                    },
                "weather": [
                    {
                        "description": 'this is a description.'
                    }
                ],
            }
        get_mock.return_value = mock_response

        # WHEN
        output = get_weather('Bahia Blanca')

        # THEN
        self.assertEqual('Bahia Blanca', output['location'])
        self.assertEqual(38, output['temperature'])
        self.assertEqual(0.86, output['humidity'])
        self.assertEqual('this is a description.', output['weather_description'])
