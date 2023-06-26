import pygame

class View:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = 20
        self.screen = pygame.display.set_mode((width * self.block_size, height * self.block_size))
        pygame.display.set_caption("Snake")

    def render(self, game_state):
        self.screen.fill((0, 0, 0))

        for segment in game_state["snake"]:
            pygame.draw.rect(self.screen, (255, 255, 255), (segment[0] * self.block_size, segment[1] * self.block_size, self.block_size, self.block_size))

        pygame.draw.rect(self.screen, (255, 0, 0), (game_state["food"][0] * self.block_size, game_state["food"][1] * self.block_size, self.block_size, self.block_size))

        pygame.display.update()
