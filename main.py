import pygame
from pygame.locals import *
import pygame.freetype

# Initialize Pygame
pygame.init()
pygame.freetype.init()

pygame.display.set_caption("RoseHack Project")

gameFont = pygame.freetype.Font("fonts/SourGummy.ttf", 24)

# Set up the drawing window
intiailWidth = 800
initialHeight = 600
screen = pygame.display.set_mode((initialHeight, intiailWidth))

# Run until the user asks to quit
running = True
while running:

  # Did the user click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the background with white
  screen.fill((255, 255, 255))

  # Draw a solid blue circle in the center
  pygame.draw.circle(screen, (0, 0, 255), (intiailWidth//2, initialHeight//2), 75)

  # Flip the display
  pygame.display.flip()

pygame.freetype.quit()
pygame.quit()