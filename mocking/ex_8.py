import unittest
from unittest.mock import patch
from message_generator import get_message


# Enter your solution here
class TestGetMessage(unittest.TestCase):
    @patch('message_generator.get_today_name', return_value='Friday')
    def test_get_message_with_friday(self, today_name_mock):
        self.assertEqual('Hello Friday!', get_message())