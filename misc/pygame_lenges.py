
import pygame
import math
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

ratio_r = .2
ratio_g = .3
ratio_b = .4

i = 0

screen_x = 1000
screen_y = 800

pygame.init()

size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Szines bigyó")

done = False

clock = pygame.time.Clock()

sin = []
cos = []
rad_to_deg=math.pi/180
for i in range(360):
    sin.append(math.sin(i*rad_to_deg))
    cos.append(math.cos(i*rad_to_deg))

screen.fill(WHITE)
pygame.display.flip()

half_x = screen_x // 2
half_y = screen_y // 2

old_x = 0
old_y = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    i += 1
    #print(i)

    color_r = ((i+120)*ratio_r) % 255
    color_g = ((i+120)*ratio_g) % 255
    color_b = ((i+120)*ratio_b) % 255
    color = (color_r, color_g, color_b)

    # radians_x = i / 56
    # radians_y = i / 47
    # x = int( (screen_x/2-10) * math.sin(radians_x)) + screen_x // 2
    # y = int( (screen_y/2-10) * math.cos(radians_y)) + screen_y // 2

    deg_x = i * .3924
    deg_y = i * .4273

    #x = int(half_x * sin[deg_x] + half_x )
    #y = int(half_y * cos[deg_y] + half_y )


    if i % 5 == 0 :
        x = int( half_x * math.sin(math.radians(deg_x)) + half_x)
        y = int( half_y * math.cos(math.radians(deg_y)) + half_y)
        pygame.draw.line(screen, color, [old_x,old_y], [x,y],3)
        old_x=x
        old_y=y


        pygame.display.flip()

    # --- Limit to 60 frames per second
    #clock.tick(600)

# Close the window and quit.
pygame.quit()