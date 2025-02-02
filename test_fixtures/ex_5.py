import unittest


class Container:
    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return f"Container(category='{self.category}')"


class TestContainer(unittest.TestCase):
    # Enter your solution here
    def setUp(self):
        self.container = Container('plastic')

    def test_init_method(self):
        msg = (
            'The container instance does not have a category '
            'attribute.'
        )
        self.assertTrue(
            hasattr(self.container, 'category'), msg
        )  # Modify this code
        self.assertEqual(
            self.container.category, 'plastic'
        )  # Modify this code

    def test_repr_method(self):
        self.assertEqual(
            repr(self.container), "Container(category='plastic')"
        )  # Modify this code
