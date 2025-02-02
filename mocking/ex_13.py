import unittest
from unittest.mock import patch
from employees import Programmer


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer()
        for t in ['python', 'sql', 'java', 'c++', 'aws']:
            self.programmer.add_tech(t)

    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = 'python'
        actual = self.programmer.get_random_tech()
        expected = 'python'
        self.assertEqual(actual, expected)

    # Enter your solution here
    @patch.object(Programmer, 'get_random_tech')
    def test_get_random_tech_mocked_cpp(self, mock_tech):
        mock_tech.return_value = 'c++'
        actual = self.programmer.get_random_tech()
        expected = 'c++'
        self.assertEqual(actual, expected)