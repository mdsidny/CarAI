
import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
# Set up the drawing window
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width = 75
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CarAI')
clock = pygame.time.Clock()
carimage = pygame.image.load('CarAi3.jpg')
# Run until the user asks to quit

def things(thingsx,thingsy,thingsw,thingsh,color):
    pygame.draw.rect(screen, color,[thingsx,thingsy,thingsw,thingsh])


def car(x,y):
    screen.blit(carimage,(x,y))

def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_object(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display('You Crashed')

def game_loop():
    x = (display_width*0.50)
    y = (display_height*0.80)
    x_change=0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    crashed = False

        # Did the user click the window close button?
        # ...
    while not crashed:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                


        x += x_change
    # ...

        
        screen.fill(white)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty += thing_speed
        car(x,y)
        if x > display_width or x<0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
          
        pygame.display.update()
        clock.tick(60)


# Done! Time to quit.
game_loop()
pygame.quit()
quit()