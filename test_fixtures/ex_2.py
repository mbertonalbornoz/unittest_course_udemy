import sys
import unittest


class Container:
    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    @unittest.skipUnless(
        sys.platform.startswith('win'), 'Requires Windows.'
    )
    def test_requires_windows(self):
        self.assertEqual(container.code, 'XC-win')

    @unittest.skipUnless(
        sys.platform.startswith('linux'), 'Requires Linux.'
    )
    def test_requires_linux(self):
        self.assertEqual(container.code, 'XC-linux')


def setUpModule():
    global container
    container = Container()

# Enter your solution here
def tearDownModule():
    global container
    del container