
import pygame
import math
import time
import random
# a lista forgatashoz
from collections import deque
import os


screen_x = 800
screen_y = 600


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (236, 3, 252)
GRAY = (130,130,130)
BLACK = (0, 0, 0)


#pygame basic setup
pygame.init()
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Labdás cucc")

bgpic = pygame.image.load('backdrop_big.jpg').convert()
ballpic = pygame.image.load('ball.png').convert()
ballpic.set_colorkey(BLACK)




class Ball():
    #ball position
    x = 0
    y = 0

    #labda iránya
    chg_x = 0
    chg_y = 0

    #labdakép
    pic = pygame.image.load('c:/Users/trifonov/python/kukac/ball.png').convert()

done = False

while not done:

    # close-ra kattintva kilepes
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()


pygame.quit()