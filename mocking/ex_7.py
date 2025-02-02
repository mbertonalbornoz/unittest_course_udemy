import unittest
from unittest.mock import patch
from code_generator import get_code


# Enter your solution here
class TestGetCode(unittest.TestCase):
    @patch('random.randint', return_value=30)
    def test_get_code_mock_should_return_30(self, get_code_mock):
        self.assertEqual(get_code(), 'CX-30')