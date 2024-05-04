from lib.classes.Sogga import Sogga
import random
import pygame
# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

sogga_img = pygame.image.load("lib/assets/sogga.png")


sogga = Sogga("Sogga", [0, 0])
sogga.zabloing()

pygame.display.set_caption("My Pygame Window")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic

    # Render graphics
    screen.fill((255, 255, 255))

    screen.blit(sogga_img, sogga.position)
    sogga.position[0] += random.randint(-1, 1)
    sogga.position[1] += random.randint(-1, 1)

    pygame.display.flip()

# Clean up Pygame
pygame.quit()


