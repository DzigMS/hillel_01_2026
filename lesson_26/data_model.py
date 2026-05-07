import random
from datetime import datetime

from names_generator import generate_name


class PracticeFormUser:

    def __init__(self, **kwargs):
        name = generate_name(style='capital').split(' ')
        self.first_name = name[0]
        self.last_name = name[1]
        self.email = self.first_name + '.' + self.last_name + '@gmail.com'
        self.gender = random.choice(['Male', 'Female', 'Other'])
        self.mobile = random.randrange(1000000000, 9999999999)
        self.dob = datetime(random.randrange(2000, 2025), random.randrange(1, 12), 3)
        self.address = 'London'

    def __str__(self):
        return ' '.join([self.first_name, self.last_name, self.email, self.gender, str(self.mobile), str(self.dob), self.address])
