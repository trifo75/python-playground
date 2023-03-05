
import trifoGraphObjects as tgo
import pygame
import random

# paraméterek
# ennyi objektum keletkezzen
num_elements = 200

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)




pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1200, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Forgó vektor")

a = 0
r = tgo.DirectionRectangle(screen)


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here


 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    x_center = 350
    y_center = 300
    #x = 200
    #y = -200
    a += 10
    center = (350, 300)
    point = (200, -200)
    pygame.draw.line(screen, BLACK, center, [sum(tup) for tup in zip(center,point)])

    point = tgo.rotatepoint(point[0],point[1],a)

    endpoint = [sum(tup) for tup in zip(center,point)]

    pygame.draw.line(screen, RED , center, endpoint)
    pygame.draw.lines(screen,GREEN,True,((100,120),(200,300),(110,500)))

    r.chg_dir_random()
    print(r.rotated_corners)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(1)
 
# Close the window and quit.
pygame.quit()