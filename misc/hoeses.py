
import pygame
import math
import random

# alap konstansok
# ablak mérete
SCREEN_X = 800
SCREEN_Y = 600

# hópihe mozgása
# Minden körben ilyen határértékek között mozdulhat el a pihe
# ezekből lesz random szám
FLAKEMOVE_X = (-.3, +.3)
FLAKEMOVE_Y = (-.1, +.9)

# alap hópihe átmérő
FLAKE_DIA = 3

# szín beállítások
FLAKE_COLOR = (255,255,255)
BG_COLOR = (0,0,0)

# hópelyhek száma
FLAKE_NUM = 1000


#pygame basic setup
pygame.init()
size = (SCREEN_X,SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hóesés")

clock = pygame.time.Clock()

flakes = []
flaketype = []
# hópehely lista inicializálása
for fl in range(FLAKE_NUM):
    flakes.append( (random.randint(0,SCREEN_X),random.randint(0,SCREEN_Y)) )
    flaketype.append(random.randint(1,5))



done = False

def move_flake(x, y):
    """A megadott koordinátákat eltolja az alap konstansok alapján. Visszaadott érték: (new_x, new_y)"""
    new_x = x + random.uniform(FLAKEMOVE_X[0],FLAKEMOVE_X[1])
    new_y = y + random.uniform(FLAKEMOVE_Y[0],FLAKEMOVE_Y[1])
    return new_x, new_y

def draw_basic_flake(x,y, typ = 0):
    """A megadott koordinátára kirak egy hópihét. Elsőre ez egy sima pötty"""
    if typ == 1 :
        pygame.draw.circle(screen, FLAKE_COLOR, (x,y), FLAKE_DIA)
    elif typ == 2 :
        pygame.draw.circle(screen, FLAKE_COLOR, (x,y), FLAKE_DIA+1)
    elif typ == 3 :
        pygame.draw.circle(screen, FLAKE_COLOR, (x,y), FLAKE_DIA+2)
    elif typ == 4 :
        pygame.draw.circle(screen, FLAKE_COLOR, (x,y), FLAKE_DIA+3)
    elif typ == 4 :
        pygame.draw.circle(screen, FLAKE_COLOR, (x,y), FLAKE_DIA+4)



#feher ures kepernyo
screen.fill(BG_COLOR)
pygame.display.flip()

# a tényleges tevékenységet végző ciklus. Addig fut, amíg meg nem jelenik
# a "pygame.QUIT" event, vagyis katt az ablakon az "X"-re

while not done:

    # close-ra kattintva kilepes
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True

    # számolós rész
    for fl in range(len(flakes)):
        flakes[fl] = move_flake(flakes[fl][0],flakes[fl][1])
        if flakes[fl][0] > SCREEN_X :
            flakes[fl] = ( 10, flakes[fl][1])
        elif flakes[fl][1] <= 0 :
            flakes[fl] = ( SCREEN_X, flakes[fl][1])

        if flakes[fl][1] > SCREEN_Y :
            flakes[fl] = ( flakes[fl][0],0)
        elif flakes[fl][1] < 0 :
            flakes[fl] = ( flakes[fl][0],SCREEN_Y)



    # rajzolós rész
    screen.fill(BG_COLOR)

    for fl in range(len(flakes)):
        draw_basic_flake(flakes[fl][0],flakes[fl][1],flaketype[fl])


    # és végül a screen-en megjelenítünk mindent, amit eddig rajzoltunk
    pygame.display.flip()

    # sebesség beállítása
    clock.tick(120)

# Ha kiléptünk a ciklusból, eldobjuk az ablakot
pygame.quit()
