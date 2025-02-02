import unittest
from unittest.mock import patch
from employees import Programmer


class TestProgrammer(unittest.TestCase):
    def setUp(self):
        self.programmer = Programmer()
        for t in ['python', 'sql', 'java', 'c++', 'aws']:
            self.programmer.add_tech(t)

    @patch.object(Programmer, 'get_random_tech')
    def test_display_random_tech_mocked_python(self, mock_tech):
        mock_tech.return_value = 'python'
        result = self.programmer.display_random_tech()
        self.assertEqual(result, 'Technology name: python')

    # Enter your solution here
    @patch.object(Programmer, 'get_random_tech')
    def test_display_random_tech_mocked_cpp(self, mock_tech):
        mock_tech.return_value = 'c++'
        result = self.programmer.display_random_tech()
        self.assertEqual(result, 'Technology name: c++')
