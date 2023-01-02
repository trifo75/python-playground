
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
 
pygame.display.set_caption("Szaladgáló bigyók")


# grafikus elemek feltöltése
# az objectlist listahoz adogatjuk hozzá véletlenszerűen a
# köröket vagy négyzeteket. Mindegyik kap random irányt.
# a random irány lehet, hogy jobb lenne konstruktorként...
objectlist = []
for o in range(num_elements):

    if random.getrandbits(1):
        newobject = tgo.Rectangle(screen)
        newobject.color = RED
        newobject.speed = 5
        #newobject.randomize_speed = False
    else:
        newobject = tgo.Circle(screen)
        newobject.color = GREEN
        newobject.speed = 2
        #newobject.randomize_dir = False
        newobject._bounce = newobject._bouncewrap1

    newobject.dir = random.random() * 360
    
    objectlist.append(newobject)
    


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
    for i, object in enumerate(objectlist):
        object.move()
        object.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()