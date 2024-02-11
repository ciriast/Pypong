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

        self.pixel_size_width = 120
        self.pixel_size_height = 10
      
        self.position_x = WIDTH // 2
        self.position_y = HEIGHT - self.pixel_size_height

        self.rectangle = pygame.Rect(self.position_x, self.position_y, self.pixel_size_width, self.pixel_size_height)

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                keys = pygame.key.get_pressed()

                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.position_x < WIDTH - self.pixel_size_width):
                    self.position_x += 15
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.position_x > 0):
                    self.position_x -= 15
                    
            self.rectangle.x = self.position_x
            self.rectangle.y = self.position_y
            
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, self.random_color, self.rectangle)
            pygame.display.flip()

    def update_screen(self):
        pygame.display.flip()

game = PyPongGame()
game.run_game()