from game import Game
from view import View
from controller import Controller

def main():
    game = Game(20, 20)
    view = View(20, 20)
    controller = Controller()

    while True:
        direction = controller.get_input()

        if direction == "quit":
            break

        game.update(direction)

        if game.is_game_over():
            break

        game_state = {
            "snake": game.snake.get_body_positions() + [game.snake.get_head_position()],
            "food": game.food.get_position()
        }

        view.render(game_state)

    print(f"Game over! Your score is {game.get_score()}")

if __name__ == "__main__":
    main()
