from snake import Snake
from food import Food

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(width // 2, height // 2)
        self.food = Food()
        self.score = 0

    def update(self, direction):
        self.snake.move(direction)

        if self.snake.get_head_position() == self.food.get_position():
            self.snake.grow()
            self.food.generate()
            self.score += 1

    def is_game_over(self):
        head_position = self.snake.get_head_position()
        body_positions = self.snake.get_body_positions()

        if (
            head_position[0] < 0 or
            head_position[0] >= self.width or
            head_position[1] < 0 or
            head_position[1] >= self.height or
            head_position in body_positions
        ):
            return True

        return False

    def get_score(self):
        return self.score
