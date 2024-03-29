import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,175)

AppleThickness = 30

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slithering Snake')

clock = pygame.time.Clock()

block_size = 20

FPS = 17

appleimg = pygame.image.load('/home/david/Desktop/.vscode/apple.png')

direction = "right"

smallfont = pygame.font.SysFont("comicsanms", 25)
medfont = pygame.font.SysFont("comicsanms", 50)
largefont = pygame.font.SysFont("comicsanms", 80)

def pause():
    paused = True
    message_to_screen("Paused",
                        black,
                        -100,
                        size="large")

    message_to_screen("Press C to continue or Q to quit",
                        black,
                        25,
                        size='small')
    pygame.display.update()

    while paused == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        clock.tick(5)

def randAppleGen(): 
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Slithering Snake",
                            green,
                            -100,
                            "large")
        message_to_screen("The objective of the game is to eat red apples",
                            black,
                            -30)

        message_to_screen("The more apples you eat, the longer you get",
                            black,
                            10)
        
        message_to_screen("If you run into yourself, or the edges, you die",
                            black,
                            50)

        message_to_screen("Press C to play, P to pause, and Q to quit",
                            black,
                            180)

        pygame.display.update()
        clock.tick(15)

def snake(snakelist,block_size):
    if direction == "right":
        snakeheadimg = pygame.image.load('/home/david/Desktop/.vscode/snakehead1.png')


    if direction == "left":
        snakeheadimg = pygame.image.load('/home/david/Desktop/.vscode/snakehead3.png')

    if direction == "up":
        snakeheadimg = pygame.image.load('/home/david/Desktop/.vscode/snakehead2.png')
    
    if direction == "down":
        snakeheadimg = pygame.image.load('/home/david/Desktop/.vscode/snakehead4.png')

    
    gameDisplay.blit(snakeheadimg, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction

    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX,randAppleY = randAppleGen()

    while not gameExit:

        if gameOver == True:        

            
            message_to_screen("Game Over", 
                                red, 
                                -50, 
                                "large")
            message_to_screen("Press C to play again or Q to quit",
                                black, 
                                50,
                                "medium")
            pygame.display.update()

        while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_c:
                            gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
            
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        AppleThickness = 30
        gameDisplay.blit(appleimg, [randAppleX, randAppleY])
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness,AppleThickness])
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(snakeList, block_size)

        message_to_screen("Score: "+str(snakeLength-1),
                            black,
                            -280)

        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1

        #frames
        clock.tick(FPS)

    if gameExit == True:
        pygame.quit()
        quit()

game_intro()
gameLoop()