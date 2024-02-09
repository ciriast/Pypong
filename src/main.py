import pygame
import random
from settings import WIDTH, HEIGHT

class PyPongGame:
    def __init__(self):
        pygame.init()
        self.size = (WIDTH, HEIGHT)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("My Pypong Game")
        self.running = True

        self.random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.pixel_size = 100
      
        self.position_x = WIDTH // 2
        self.position_y = HEIGHT // 2

        self.rectangle = pygame.Rect(self.position_x, self.position_y, self.pixel_size, self.pixel_size)

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.position_x += 10
                    elif event.key == pygame.K_LEFT:
                        self.position_x -= 10
                    elif event.key == pygame.K_a:
                        print("Move left")
                    elif event.key == pygame.K_d:
                        print("Move right")

            self.rectangle.x = self.position_x
            self.rectangle.y = self.position_y
            
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, self.random_color, self.rectangle)
            pygame.display.flip()

    def update_screen(self):
        pygame.display.flip()

game = PyPongGame()
game.run_game()