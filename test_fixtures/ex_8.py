import unittest
import tempfile


class FileReader:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.read()


# Enter your solution here
class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file.write('Hello, world!')
        self.temp_file.close()

    def tearDown(self):
        import os
        os.unlink(self.temp_file.name)

    def test_read_file(self):
        r = FileReader()
        self.assertEqual('Hello, world!', r.read_file(self.temp_file.name))
