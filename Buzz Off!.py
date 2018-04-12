#!/usr/bin/env python
#
# Buzz Off!
# A simple platforming/puzzle game by Jeff and Zach
# credit to Dev for photography and design help
#**website here**
#

import pygame, sys
#from mainmenu import MainMenu, Settings, Audio, Video
#from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
#sets window name
pygame.display.set_caption('Buzz Off!')
clock = pygame.time.Clock()

#sets window resolution
display_width = 800
display_height = 720
gameDisplay = pygame.display.set_mode((display_width,display_height))


    

# from https://python-forum.io/Thread-PyGame-Creating-a-state-machine

class States(object):
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'game'
    def cleanup(self):
        print('cleaning up Menu state stuff')
    def startup(self):
        print('starting Menu state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Menu State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((255,0,0))
  
class Game(States):
    def __init__(self):
        States.__init__(self)
        self.next = 'menu'
    def cleanup(self):
        print('cleaning up Game state stuff')
    def startup(self):
        print('starting Game state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            print('Game State keydown')
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,255))
  
class Control:
    def __init__(self, **settings):
        self.__dict__.update(settings)
        self.done = False
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
    def flip_state(self):
        self.state.done = False
        previous,self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous
    def update(self, dt):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, dt)
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.state.get_event(event)
    def main_game_loop(self):
        while not self.done:
            delta_time = self.clock.tick(self.fps)/1000.0
            self.event_loop()
            self.update(delta_time)
            pg.display.update()

# controller
controller_mode = False
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count > 0:
    controller_mode = True
if controller_mode == True:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    axes = joystick.get_numaxes()
    controllerbuttons = joystick.get_numbuttons()
    Joystick1State = [False,False,False,False]
    ButtonStates = [0,0,0,0,0,0,0,0,0,0,0,0]
    InitialButtons = [0,0,0,0,0,0,0,0,0,0,0,0]

#sets Gameboy colors
Darkest_Green = (15, 56, 15)
Dark_Green = (48, 98, 48)
Light_Green = (139, 172, 15)
Lightest_Green = (155, 188, 15)




BeeImg = pygame.image.load('Bee_clone.png').convert_alpha()

def Bee (x,y):
    gameDisplay.blit (BeeImg, (x,y))


x = (display_width * 0.5)
y = (display_width * 0.82)

x_change = 0

# Functions

def normalize(num,amount):
    if abs(num) < amount:
        num = 0
    elif num < 0:
        num += amount
    elif num > 0:
        num -= amount
    return num

def cap(num,amount):
    if num > amount:
        num = amount
    if num < -amount:
        num = -amount
    return num

def maximum(num,amount):
    if num > amount:
        num = amount
    return num

def minimum(num,amount):
    if num < amount:
        num = amount
    return num

'''def game_intro():

     intro = True
     while intro:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             if event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   return
             if event.type == pygame.KEYDOWN:
                intro = False
                
         gameDisplay.fill(Darkest_Green)
         largeText = pygame.font.Font('Early GameBoy.ttf', 50)
         TextSurf, TextRect = text_objects("Buzz Off!", largeText)
         TextRect.center = ((display_width/2), (display_height/3))
         gameDisplay.blit (TextSurf, TextRect)

         
         
         largeText = pygame.font.Font('Early GameBoy.ttf', 25)
         TextSurf, TextRect = text_objects("Press Any Key To Start", largeText)
         TextRect.center = ((display_width/2), (display_height/1.5))
         gameDisplay.blit (TextSurf, TextRect)
         pygame.display.update()



            

def text_objects(text, font):
    textSurface = font.render(text, True, Lightest_Green)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('Early GameBoy.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/3))
    gameDisplay.blit (TextSurf, TextRect)

game_loop() '''

#Variables
crashed = False


while not crashed:
    
#controls
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            crashed = True
        if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   pygame.quit()
        #game_intro()
        
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x_change = -0.13
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x_change = 0.13
            if event.key == pygame.K_ESCAPE:
                sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                x_change = 0
    
    x += x_change 
            
    gameDisplay.fill(Lightest_Green)
    Bee (x,y)
    



    
    pygame.display.update()
    


