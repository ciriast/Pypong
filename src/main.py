import pygame
import random

WIDTH = 800
HEIGHT = 600

class PyPongGame:
    def __init__(self):
        pygame.init()
        self.size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My Pypong Game")
        self.running = True

        random_x = random.randint(0, WIDTH)
        random_y = random.randint(0, HEIGHT)
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.screen.set_at((random_x, random_y), (random_color))
        
    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()

game = PyPongGame()
game.run_game()