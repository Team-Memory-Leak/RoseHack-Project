import pygame
import os

# Initialize Pygame
pygame.init()
pygame.freetype.init()

pygame.display.set_caption("RoseHack Project")

gameFont = pygame.freetype.Font("fonts/SourGummy.ttf", 24)

# Initial window size
width = 1600
height = 1150

# Create a resizable display
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("RoseHack Project")
clock = pygame.time.Clock()
running = True
score = 0

# Load the image once
background = pygame.image.load('Images/Rosehack Bg Project.png')

# Scale the image initially
background = pygame.transform.scale(background, (width, height))

def defaultButton(width, height, x, y, text, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global score

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            while click[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        click = pygame.mouse.get_pressed()
                clock.tick(60)
            print("Button Clicked")
            score += 1
            print(score)
            
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    text_surface, text_rect = font.render(text, (0, 0, 0), size=40)
    text_rect.center = (x + width / 2, y + height / 2)
    screen.blit(text_surface, text_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle window resize event
        if event.type == pygame.VIDEORESIZE:
            width, height = event.size  # Update the dimensions
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            background = pygame.transform.scale(background, (width, height))  # Rescale the background

    # Draw the image onto the screen
    screen.blit(background, (0, 0))

    # Draw the button
    defaultButton(200, 50, (width - 200)//2, (height - 50)//2, "Start", ("white"), (0, 200, 0), gameFont)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()