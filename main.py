import pygame
import random

# Initialize Pygame
pygame.init()
pygame.freetype.init()

pygame.display.set_caption("RoseHack Project")

englishDictionary = open("diction/EnglishDictionary", "r")
imageHash = open("diction/ImageHash", "r")
japaneseDictionary = open("diction/JapaneseDictionary", "r")

englishDictionary = englishDictionary.read().split("\n")
imageHash = imageHash.read().split("\n")
japaneseDictionary = japaneseDictionary.read().split("\n")

count = 0
historyIndex = -1
  
gameFont = pygame.freetype.Font("fonts/SourGummy.ttf", 24)
gameFont2 = pygame.freetype.Font("fonts/KiwiMaru.ttf", 40)


#Inititial window size 
width = 1600
height = 1150
# Create a resizable display
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("RoseHack Project")
clock = pygame.time.Clock()
running = True
score = 0
button_visible = True
background = pygame.image.load("Images/Rosehack Bg Project.png")

background = pygame.transform.scale(background, (width, height))

def defaultButton(width, height, x, y, text, color, hover_color, font, font_size):
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

    text_surface, text_rect = font.render(text, (0, 0, 0), size=font_size)
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
        defaultButton(200, 50, (width - 200)//2, (height - 50)//2, "Play", ("white"), (0, 200, 0), gameFont, 40)
        defaultDisplay(600, 200, (width - 600)//2, (height - 600)//2, "NihonGo", ("light green"), gameFont2, 90, "black")

    elif not button_visible:
        hint = False #Hint is not visible 
        #To implement this we may need to make the button function to return a value when it is clicked either true or false or we could add another function for 
        #buttons that return a value when clicked

        while count != 2:
            correlatedIndex = random.randint(0, len(englishDictionary))
            while correlatedIndex == historyIndex:
                correlatedIndex = random.randint(0, len(englishDictionary))
            print(imageHash[correlatedIndex])
            print(japaneseDictionary[correlatedIndex])

            option1 = random.randint(0, len(englishDictionary) - 1)
            option2 = random.randint(0, len(englishDictionary) - 1)

            while option1 == correlatedIndex or option1 == historyIndex:
                option1 = random.randint(0, len(englishDictionary) - 1)
            while option2 == correlatedIndex or option2 == option1 or option2 == historyIndex:
                option2 = random.randint(0, len(englishDictionary) - 1)

            print("Which of the following is the correct translation of the word above?")

            possibleAnswers = [englishDictionary[correlatedIndex],englishDictionary[option1], englishDictionary[option2]]
            random.shuffle(possibleAnswers)

            count += 1
            historyIndex = correlatedIndex

            #pygame.time.wait(2000)

        defaultButton(400, 150, (width - 600)//2, (height + 500)//2, englishDictionary[0], ("white"), (0, 200, 0), gameFont, 40) #Bottom Right
        defaultButton(400, 150, (width - 1520)//2, (height + 500)//2, "Default3", ("white"), (0, 200, 0), gameFont, 40) #Bottom Left
        defaultButton(400, 150, (width - 600)//2, (height - 150)//2, "Default2", ("white"), (0, 200, 0), gameFont, 40) #Top Right
        defaultButton(400, 150, (width - 1520)//2, (height - 150)//2, "Default1", ("white"), (0, 200, 0), gameFont, 40) #Bottom Left
        
        defaultButton(300, 100, (width - 950)//2, (height - 650)//2, "Hint?", ("white"), (0, 200, 0), gameFont, 40)#Hint button
        defaultDisplay(700, 100, (width - 1350)//2, (height - 400)//2, "Which is the correct translation of the word on the right?", ("white"), gameFont, 25, "black")#Hint button

        defaultDisplay(300, 100, (width - 1400)//2, height - 1050 , "Streak:", ("white"), gameFont, 40, "black")#Streak Button
        defaultDisplay(300, 100, (width - 500)//2, height - 1050 , "Top Streak:", ("white"), gameFont, 40, "black")#High Score Button
        
        imageDisplay(550, 500, (width + 350)//2, height - 630, "Images/answers/ocean.jpg")

        defaultDisplay(550, 100, (width +350)//2, height - 1050 , "Hiragana", ("white"), gameFont, 40, "black")#High Score Button
        defaultDisplay(550, 300, (width +350)//2, height - 940 , "Japanese", ("white"), gameFont, 80, "black")#High Score Button
        
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
