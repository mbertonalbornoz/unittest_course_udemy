import unittest
from unittest.mock import MagicMock, patch
from advanced_mocking.my_module import fetch_data, get_average_value


@patch('requests.get')
class TestMyModule(unittest.TestCase):
    def setUp(self):
        self.expected_data = [
            {"value": 1},
            {"value": 2},
            {"value": 3}
        ]
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = self.expected_data

    def test_fetch_data(self, get_mock):
        # GIVEN
        get_mock.return_value = self.mock_response

        # WHEN
        data = fetch_data()

        # THEN
        self.assertEqual(self.expected_data, data)

    def test_get_average_value(self, get_mock):
        # GIVEN
        get_mock.return_value = self.mock_response
        data = fetch_data()
        data_1 = [
            {"value": 1},
            {"other_field": 2},
            {"value": 3}
        ]
        data_2 = []

        # WHEN
        avg = get_average_value(data, 'value')
        avg_1 = get_average_value(data_1, 'value')
        avg_2 = get_average_value(data_2, 'value')

        # THEN
        self.assertEqual(2.0, avg)
        self.assertEqual(2.0, avg_1)
        self.assertEqual(None, avg_2)
