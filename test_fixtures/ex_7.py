import unittest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


# Enter your solution here
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.c = Calculator()

    def tearDown(self):
        del self.c

    def test_add(self):
        self.assertEqual(self.c.add(1, 3), 4)

    def test_subtract(self):
        self.assertEqual(self.c.subtract(1, 3), -2)