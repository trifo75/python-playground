
import pygame
import random

# ekkora ablakot nyitunk
SCREEN_X = 1800
SCREEN_Y = 900

# frissítés sebessége
FPS = 5

# háttérszín, halott sejt színe, élő sejt színe
COLOR_BG = (0,0,0)
COLOR_LIVE = (0,200,0)
COLOR_DEAD = (0,60,0)

# sejt mérete, sarkainak lekerekítése, sejtek közötti térköz
CELL_SIZE = 20
CELL_RAD = 5
CELL_BORDER = 3

# sejtek száma vízszintesen és függőlegesen
CELL_X = SCREEN_X // CELL_SIZE
CELL_Y = SCREEN_Y // CELL_SIZE

# indításkor ennyi esélye van egy sejtnek, hogy élőként kökkön létre
LIVE_TRESHOLD = .075

# sejteket tartalmazó tömb létrehozása
cells = [[0 for i in range(CELL_X)] for j in range(CELL_Y)]

# sejtek inicializálása a TRESHOLD alapján
for row in range(len(cells)):
    for col in range(len(cells[row])):
        cells[row][col] = 0 if random.random() > LIVE_TRESHOLD else 1

#pygame basic setup
pygame.init()
size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Life")


done = False


clock = pygame.time.Clock()

#üres képernyő
screen.fill(COLOR_BG)
pygame.display.flip()

# a tényleges tevékenységet végző ciklus. Addig fut, amíg meg nem jelenik
# a "pygame.QUIT" event, vagyis katt az ablakon az "X"-re

while not done:

    # close-ra kattintva kilepes
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True

    # cellák újraszámolása
    old_cells = cells
    for row in range(len(cells)):
        for col in range(len(cells[row])):
            #szomszédok összeszámolása
            #mindegyikre rápróbálunk külön, mert különben a tábla szélén
            #lévő segteknél IndexError lenne
            live_neighbors = 0

            for cy in [-1,0,1]:
                for cx in [-1, 0, 1]:
                    #print(col,row,cx,cy)
                    if cx == 0 and cy == 0: # önmagát nem vizsgáljuk
                        continue
                    if cy+row <0 or cy+row >= CELL_Y : # a táblán túl van
                        continue
                    if cx+col <0 or cx+col >= CELL_X : # a táblán túl van
                        continue

                    live_neighbors = live_neighbors + old_cells[row+cy][col+cx]



            # A szabályok levizsgálása
            # ha a sejt él és...
            if old_cells[row][col] :
                #... 2-nék kevesebb, vagy 3-nál több szomszédja van, akkor haljon meg
                if live_neighbors < 2 or live_neighbors > 3:
                    cells[row][col] = 0
            # ha a sejt halott...
            else:
                #... és pontosan 3 szomszédja él, akkor támadjon fel
                if live_neighbors == 3:
                    cells[row][col] = 1
    if cells == old_cells:
        print("Life game stalled, exiting.")
        #done = True



    # cellák kirajzolása
    for row,cellrow in enumerate(cells):
        for col,cell in enumerate(cellrow):
            if cell :
                color = COLOR_LIVE
            else:
                color = COLOR_DEAD
            # egy sejt kirajzolása
            pygame.draw.rect(screen,color,(col*CELL_SIZE + CELL_BORDER,row*CELL_SIZE + CELL_BORDER,CELL_SIZE - CELL_BORDER *2 ,CELL_SIZE - CELL_BORDER *2), border_radius = CELL_RAD)



    # és végül az egészet kidobjuk a screen-re
    pygame.display.flip()
    clock.tick(FPS)



pygame.quit()