import unittest
from unittest.mock import patch
from code_generator import get_code_with_day


# Enter your solution here
class TestGetCodeWithDay(unittest.TestCase):
    @patch('random.randint', return_value=5)
    @patch('code_generator.get_today_name', return_value='FRI')
    def test_get_code_with_day_with_mocked_friday(self, mock_day, mock_int):
        actual = get_code_with_day()
        expected = 'CX-5-FRI'
        self.assertEqual(expected, actual)