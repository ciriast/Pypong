import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Pypong game")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False