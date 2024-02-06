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

        self.medium_x = WIDTH // 2
        self.medium_y = HEIGHT // 2
        self.random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.pixel_size = 100

        self.draw_pixel()

    def draw_pixel(self):
        pygame.draw.rect(self.screen, self.random_color, (self.medium_x, self.medium_y, self.pixel_size, self.pixel_size))

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print("Move right")
                    elif event.key == pygame.K_LEFT:
                        print("Move left")
                    elif event.key == pygame.K_a:
                        print("Move left")
                    elif event.key == pygame.K_d:
                        print("Move right")
            self.update_screen()

    def update_screen(self):
        pygame.display.flip()

game = PyPongGame()
game.run_game()