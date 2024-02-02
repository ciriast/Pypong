import pygame
import random

class PyPongGame:
    def __init__(self):
        pygame.init()
        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My Pypong Game")
        self.running = True

    def run_game(self):
        while self.running:
            my_x = random.randint(0, 800-1)
            my_y = random.randint(0, 600-1)

            pixel = random.randint(0, 255)

            self.screen.set_at((my_x, my_y), (pixel))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()

game = PyPongGame()
game.run_game()