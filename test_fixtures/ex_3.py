import sys
import unittest


class Container:
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    # Enter your solution here
    @classmethod
    def setUpClass(cls):
        cls.container = Container()

    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        self.assertEqual(
            self.container.code, 'XC-win'
        )  # Code to modify

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        self.assertEqual(
            self.container.code, 'XC-linux'
        )  # Code to modify
