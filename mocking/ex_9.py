import unittest
from unittest.mock import patch
from message_generator import get_message


class TestGetMessage(unittest.TestCase):
    @patch('message_generator.get_today_name')
    def test_get_message_with_friday(self, mock_day):
        mock_day.return_value = 'Friday'
        actual = get_message()
        expected = 'Hello Friday!'
        self.assertEqual(actual, expected)

    # Enter your solution here
    @patch('message_generator.get_today_name', return_value='Monday')
    def test_get_message_with_monday(self, mock_day):
        self.assertEqual('Hello Monday!', get_message())