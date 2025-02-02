import unittest
from unittest.mock import patch

from employees import Programmer


# Enter your solution here
class TestProgrammer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.programmer = Programmer()
        for t in ['python',  'sql',  'java',  'c++',  'aws']:
            cls.programmer.add_tech(t)

    @patch.object(Programmer, 'get_random_tech', return_value='python')
    def test_get_random_tech_mocked_python(self, get_random_tech_mock):
        self.assertEqual('python', self.programmer.get_random_tech())


