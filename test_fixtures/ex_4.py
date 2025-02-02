import sys
import unittest


class Container:
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.container = Container()

    # Enter your solution here
    @classmethod
    def tearDownClass(cls):
        del cls.container

    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        self.assertEqual(self.container.code, 'XC-win')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        self.assertEqual(self.container.code, 'XC-linux')
