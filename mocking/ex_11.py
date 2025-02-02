import unittest
from unittest.mock import patch
from code_generator import get_code_with_day


class TestGetCodeWithDay(unittest.TestCase):
    @patch('code_generator.get_today_name')
    @patch('random.randint')
    def test_get_code_with_day_with_mocked_friday(
        self, mock_int, mock_day
    ):
        mock_int.return_value = 30
        mock_day.return_value = 'FRI'
        actual = get_code_with_day()
        expected = 'CX-30-FRI'
        self.assertEqual(actual, expected)

    # Enter your solution here
    @patch('random.randint', return_value=20)
    @patch('code_generator.get_today_name', return_value='MON')
    def test_get_code_with_day_with_mocked_monday(self, mock_day, mock_int):
        expected = 'CX-20-MON'
        actual = get_code_with_day()
        self.assertEqual(expected, actual)