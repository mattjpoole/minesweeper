import pygame 
from pygame.locals import *
import json 
  
# Take colors input// 
YELLOW = (255, 255, 0) 
BLUE = (0, 0, 255) 
  
  
# initial data values 
data = { 
    'pos_x': 320, 
    'pos_y': 175
} 
  
try: 
    # the file already exists 
    with open('prev_pos.txt') as load_file: 
        data = json.load(load_file) 
except: 
    # create the file and store initial values 
    with open('prev_pos.txt', 'w') as store_file: 
        json.dump(data, store_file) 
  
  
# Construct the GUI game// 
pygame.init() 
  
# Set dimensions of game GUI// 
w, h = 1200, 600
screen = pygame.display.set_mode((w, h)) 
  
# Take image as input// 
img = pygame.image.load('./images/one.png') 
img.convert() 
  
# Draw rectangle around the image// 
rect = img.get_rect() 
rect.center = data["pos_x"], data["pos_y"] 
  
# Set running and moving values// 
running = True
moving = False
  
# Setting what happens when game 
# is in running state 
while running: 
  
    for event in pygame.event.get(): 
  
        # Close if the user quits the 
        # game 
        if event.type == QUIT: 
            with open('prev_pos.txt', 'w') as store_data: 
                json.dump(data, store_data) 
  
            running = False
  
        # Making the image move 
        elif event.type == MOUSEBUTTONDOWN: 
            if rect.collidepoint(event.pos): 
                moving = True
  
        # Set moving as False if you want 
        # to move the image only with the 
        # mouse click 
        # Set moving as True if you want 
        # to move the image without the 
        # mouse click 
        elif event.type == MOUSEBUTTONUP: 
            moving = False
  
        # Make your image move continuously 
        elif event.type == MOUSEMOTION and moving: 
            rect.move_ip(event.rel) 
            data["pos_x"] = event.pos[0] 
            data["pos_y"] = event.pos[1] 
  
    # Set screen color and image on screen 
    screen.fill(YELLOW) 
    screen.blit(img, rect) 
  
    # Construct the border to the image 
    pygame.draw.rect(screen, BLUE, rect, 2) 
  
    # Update the GUI pygame 
    pygame.display.update() 
  
  
# Quit the GUI game 
pygame.quit() 