import pygame
import os

# Initialize Pygame
pygame.init()
pygame.freetype.init()

pygame.display.set_caption("RoseHack Project")

gameFont = pygame.freetype.Font("fonts/SourGummy.ttf", 24)
gameFont2 = pygame.freetype.Font("fonts/KiwiMaru.ttf", 40)

# Initial window size
width = 1600
height = 1150

# Create a resizable display
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("RoseHack Project")
clock = pygame.time.Clock()
running = True
score = 0
button_visible = True

# Load the image once
background = pygame.image.load('Images/Rosehack Bg Project.png')

# Scale the image initially
background = pygame.transform.scale(background, (width, height))



def defaultButton(width, height, x, y, text, color, hover_color, font):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global score, button_visible
    

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            while click[0] == 1:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        click = pygame.mouse.get_pressed()
                clock.tick(60)
            button_visible = False
                
            
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    text_surface, text_rect = font.render(text, (0, 0, 0), size=40)
    text_rect.center = (x + width / 2, y + height / 2)
    screen.blit(text_surface, text_rect)

def defaultDisplay(width, height, x, y, text, color, font, font_size, textColor):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface, text_rect = font.render(text, (textColor), size=font_size)
    text_rect.center = (x + width / 2, y + height / 2)
    screen.blit(text_surface, text_rect)

def imageDisplay(width, height, x, y, image):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (width, height))
    screen.blit(image, (x, y))

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
    if button_visible:
        defaultButton(200, 50, (width - 200)//2, (height - 50)//2, "Play", ("white"), (0, 200, 0), gameFont)
        defaultDisplay(600, 200, (width - 600)//2, (height - 600)//2, "NihonGo", ("light green"), gameFont2, 90, "black")

    elif not button_visible:
        hint = False #Hint is not visible 
        #To implement this we may need to make the button function to return a value when it is clicked either true or false or we could add another function for 
        #buttons that return a value when clicked

        defaultButton(300, 150, (width - 500)//2, (height + 500)//2, "Default4", ("white"), (0, 200, 0), gameFont) #Bottom Right
        defaultButton(300, 150, (width - 1400)//2, (height + 500)//2, "Default3", ("white"), (0, 200, 0), gameFont) #Bottom Left
        defaultButton(300, 150, (width - 500)//2, (height - 150)//2, "Default2", ("white"), (0, 200, 0), gameFont) #Top Right
        defaultButton(300, 150, (width - 1400)//2, (height - 150)//2, "Default1", ("white"), (0, 200, 0), gameFont) #Bottom Left

        defaultButton(300, 100, (width - 950)//2, (height - 550)//2, "Hint?", ("white"), (0, 200, 0), gameFont)#Hint button

        defaultDisplay(300, 100, (width - 1400)//2, height - 1050 , "Streak:", ("white"), gameFont, 40, "black")#Streak Button
        defaultDisplay(300, 100, (width - 500)//2, height - 1050 , "Top Streak:", ("white"), gameFont, 40, "black")#High Score Button

        #we will probably use this later
        #if hint:
        imageDisplay(550, 500, (width + 350)//2, height - 630, "Images/answers/ocean.jpg")

        #Japaneses Characters
        defaultDisplay(550, 100, (width +350)//2, height - 1050 , "Hiragana", ("white"), gameFont, 40, "black")#High Score Button
        defaultDisplay(550, 300, (width +350)//2, height - 940 , "Japanese", ("white"), gameFont, 80, "black")#High Score Button




    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()