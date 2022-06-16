
import pygame
import math
import time
import random
# a lista forgatashoz
from collections import deque
import os

print("CWD: ", os.getcwd())

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (236, 3, 252)
GRAY = (130,130,130)
BLACK = (0, 0, 0)

# a kukac indulo hossza
worm_len = 120

#kezdeti irany (fok)
dir = 110
dir_delta = 0

#kezdeti sebesseg
speed = 5
speed_delta = .2

# ennyi lepesig tartsa a jelenlegi kanyar ivet (dir_delta)
step = 0

# ütközésfolt paraméterek
crash_steps = 200
crash_delta = .6
crash_color_from = RED
crash_color_to = WHITE
crash = []

# a crash_color_from és crash_color_to értékek között interpolálva feltöltünk egy
# listát, crash_steps darab elemmel. Ez lesz a színáátmenet, ami a falnak ütközéskor megjelenik
crash_color = []
for c in range(crash_steps):
    c0 = int(crash_color_to[0] + (crash_color_from[0]-crash_color_to[0]) * c / ( crash_steps -1 ))
    c1 = int(crash_color_to[1] + (crash_color_from[1]-crash_color_to[1]) * c / ( crash_steps -1 ))
    c2 = int(crash_color_to[2] + (crash_color_from[2]-crash_color_to[2]) * c / ( crash_steps -1 ))
    crash_color.append((c0,c1,c2))

i = 0

screen_x = 1200
screen_y = 800

#pygame basic setup
pygame.init()
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Szines bigyó")

bgpic = pygame.image.load('c:/Users/trifonov/python/kukac/backdrop_big.jpg').convert()
ballpic = pygame.image.load('c:/Users/trifonov/python/kukac/ball.png').convert()
ballpic.set_colorkey(BLACK)
pygame.mouse.set_visible(False)



#kukac inicializalas
#deque -be kerülnek a kukac pontjai (koordináták), mert azon van rotate
worm = deque([])

#sima listába generálódnak az egyes szakaszokhoz a szín tuple-ek
colorlist = []

# maga a feltöltés. Kezdetben a kukac minden pontja a képernyő közepére kerül
# a szín meg egyre halványabb az elejétől a vége felé
for i in range(worm_len):
    worm.append((screen_x/2,screen_y/2))
    colorlist.append((int(255*i/worm_len),255,int(255*i/worm_len)))

# taszítás mértéke
# 100 felett 0
# 100 alatt a képlet szerint
# minél közelebb van a falhoz a kukac feje, annál nagyobb szögelfordulás kell
def repel_by_dist(dist):
    if dist > 100:
        return 0
    if dist > 0:
        angle=800/(dist + 10 )
    else:
        angle = 30
    return angle


done = False


clock = pygame.time.Clock()

#feher ures kepernyo
screen.fill(WHITE)
pygame.display.flip()

# a tényleges tevékenységet végző ciklus. Addig fut, amíg meg nem jelenik
# a "pygame.QUIT" event, vagyis katt az ablakon az "X"-re

while not done:

    # close-ra kattintva kilepes
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            done = True

    # kukac mozdul
    # minden körbek kiszámoljuk a kukac elejének új koordinátáit az aktuális dir és speed értékek alapján
    color = GREEN
    delta_x = math.sin(math.radians(dir))*speed
    delta_y = math.cos(math.radians(dir))*speed
    x = worm[0][0] + delta_x
    y = worm[0][1] + delta_y

    # falnak ütközések lekezelése visszapattanás által (dir módosítása az ütközésnek megfelelően)

    # x irány vizsgálata
    # jobb oldali fal
    if x > screen_x:
        x = screen_x
        if dir >=90:
            dir = 225
            crash.append([x,y,crash_steps])
        else:
            dir = 315
            crash.append([x,y,crash_steps])
    # bal oldali fal
    elif x < 0:
        x = 0
        if dir > 270:
            dir = 45
            crash.append([x,y,crash_steps])
        else:
            dir = 135
            crash.append([x,y,crash_steps])

    # y irány vizsgálata
    # alsó fal
    if y > screen_y:
        y = screen_y
        if dir > 270:
            dir = 225
            crash.append([x,y,crash_steps])
        else:
            dir = 135
            crash.append([x,y,crash_steps])
    # felső fal
    elif y < 0:
        y = 0
        if dir > 180:
            dir = 315
            crash.append([x,y,crash_steps])
        else:
            dir = 45
            crash.append([x,y,crash_steps])


    #Taszítás a falaktól
    # az aktuális irányt figyelembe véve mind a négy faltól kiszámoljuk a
    # taszítás mértékét és azzal változtatjuk az irányt
    #jobbra le tartomány
    #balra le tartomány
    if dir>=270  :
        #           fent                 jobbra                         lent                            balra
        dir = dir + repel_by_dist( y ) - repel_by_dist( screen_x - x) - repel_by_dist( screen_y - y ) + repel_by_dist( x )
    #balra fel tartomány
    elif dir>=180 :
        #           fent                 jobbra                         lent                            balra
        dir = dir + repel_by_dist( y ) + repel_by_dist( screen_x - x) - repel_by_dist( screen_y - y ) - repel_by_dist( x )
    #jobbra fel tartomány
    elif dir>=90 :
        #           fent                 jobbra                         lent                            balra
        dir = dir - repel_by_dist( y ) + repel_by_dist( screen_x - x) + repel_by_dist( screen_y - y ) - repel_by_dist( x )
    #jobbra le tartomány
    else :
        #           fent                 jobbra                         lent                            balra
        dir = dir - repel_by_dist( y ) - repel_by_dist( screen_x - x) + repel_by_dist( screen_y - y ) + repel_by_dist( x )



    # kukacba betesszük az újonnan kiszámolt pontot, majd a legvégét eldobjuk
    worm.appendleft((x,y))
    worm.pop()

    #kukac irány
    #ha lejárt a "step" számláló, akkor random új dir_delta és speed értéket választunk
    #valamint új step értéket - hogy hány lépésig maradjon az előző kettő
    if step < 1:
        step = random.randint(5,50)
        dir_delta = random.randint(-8,8)
        speed_target = random.randint(10,22)

    if speed > speed_target:
        speed -= speed_delta
    else:
        speed += speed_delta

    # dir léptetése
    dir = dir + dir_delta

    # step léptetése
    step -= 1

    # a dir értékének korrigálása, ha a 0-360 fokos tartományból kimenne
    # biztos lehetne ezt szebben is
    if dir > 360:
        dir = dir - 360

    if dir < 0:
        dir = 360 - dir



    # kukac kirajzol
    # ciklussal végigjárjuk a worm-ban tárolt koordinátákat és megrajzoljuk a vonalakat a colorlist-ben tárolt színek szerint
    # gyanítom, hogy lehetne szebben is
    #screen.fill(WHITE)
    screen.blit(bgpic, (0,0))

    # kirajzoljuk az ütközéseket
    for cr in range(len(crash)) :
        # a kör helye az üzközés helye, ami a crash listában van ( x , y , maradék_lépés ) formában
        # a kör mérete a maradék_lépések alapján számítódik a crash_steps és crash_delta segítségével
        # a színt a maradék lépések index alapján a crash_color listából vesszük
        pygame.draw.circle(screen,crash_color[crash[cr][2]-1],(crash[cr][0],crash[cr][1]),(crash_steps-crash[cr][2])*crash_delta)

        # a maradék lépéseket minden körben csökkentjük eggyel, ha eléri a nullát, akkor a listaelem törlődik
        crash[cr][2] -= 1

        # ez igazából asszem tök felesleges
        if crash[cr][2] < 1:
            crash[cr][2] = 0

    # a crash listából törlünk minden elemet, ahol a step érték nulla
    crash = [ item for item in crash if item[2] > 0 ]

    # ez itt a kukac megrajzolása a colorlist színei alapján
    for i in range(2,len(worm)):
        pygame.draw.line(screen,colorlist[i],worm[i-1],worm[i],15)


    # rajzolunk egy piros csíkot, ami a jelenlegi irányt és sebességet reprezentálja
    pygame.draw.line(screen,RED,(100,100),(100+delta_x*5,100+delta_y*5),2)

    # sebességet megjelenítő csík
    pygame.draw.line(screen,RED,(10,10),(10+speed*10,10),10)

    #labda kirak
    mouspos = pygame.mouse.get_pos()
    screen.blit(ballpic, (mouspos[0]-60,mouspos[1]-60))

    # és végül a screen-en megjelenítünk mindent, amit eddig rajzoltunk
    pygame.display.flip()

    # sebesség beállítása
    clock.tick(120)

# Ha kiléptünk a ciklusból, eldobjuk az ablakot
pygame.quit()
