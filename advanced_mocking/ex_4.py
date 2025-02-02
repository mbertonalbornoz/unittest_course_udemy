import unittest
from unittest import mock
from weather import WeatherAPI, WeatherAnalyzer


# Enter your solution here
class TestWeatherAnalyzer(unittest.TestCase):
    def test_is_raining(self):
        # GIVEN
        weather_data = {
            'weather': [
                {
                    'main': 'Rain'
                }
            ]
        }
        weather_api = mock.MagicMock(spec=WeatherAPI)
        weather_api.get_weather.return_value = weather_data
        london_weather = weather_api.get_weather('London')
        analyzer = WeatherAnalyzer()

        # WHEN
        output = analyzer.is_raining(london_weather)

        # THEN
        self.assertTrue(True, output)