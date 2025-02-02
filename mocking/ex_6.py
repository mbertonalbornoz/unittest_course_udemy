import random
from unittest.mock import patch


class Programmer:
    def __init__(self):
        self.tech_names = []

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if name not in self.tech_names:
            self.tech_names.append(name)
        return self

    def get_random_tech(self):
        return random.choice(self.tech_names)


programmer = Programmer()
programmer.add_tech('python')
programmer.add_tech('sql')
programmer.add_tech('java')
programmer.add_tech('c++')
programmer.add_tech('aws')

# Enter your solution here
@patch('random.choice', return_value='c++')
def test_get_random_tech(random_choice_mock):
    print(programmer.get_random_tech())

test_get_random_tech()