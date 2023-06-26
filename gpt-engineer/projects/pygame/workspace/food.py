import random

class Food:
    def __init__(self):
        self.position = (0, 0)

    def generate(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def get_position(self):
        return self.position
