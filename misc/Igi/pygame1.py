import pygame
pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = ( 100, 155, 255)
YELLOW   = ( 255, 255,   0)
#ablak nyitása
size = (700, 500)
screen = pygame.display.set_mode(size)

done = False

# Itt állítjuk be, hogy a képernyő milyen rendszerességgel frissül.
clock = pygame.time.Clock()

# -------- A főprogram ciklusa -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("A felhasználó ki szeretne lépni.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("A felhasználó lenyomott egy billentyűt.")
        elif event.type == pygame.KEYUP:
            print("Felhasználó elengedett egy billentyűt.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("megnyomtál egy egérgombot")

        # A képernyő letörlése és a képernyő háttér beállítása
        # Gyerünk, és frissítsük a képernyőt azzal, amit rajzoltunk.

    alma = 0
    while alma > 3:
        if alma == 0:
            pygame.draw.line(screen, GREEN, [0,400], [1000,400], 250)
            alma+=1
        if alma ==1
            pygame.draw.line(screen, BLUE, [0,0], [1000,0], 600)
            alma+=1
        if alma ==2
            alma+=1
            pygame.draw.line(screen, YELLOW, [500,100], [550,100], 50)





        # Gyerünk, és frissítsük a képernyőt azzal, amit rajzoltunk.
    pygame.display.flip()
    # A játék logikája a komment alatt folytatódik
    #  A játék logikája a komment alatt folytatódik


    #  A játék logikája a komment alatt folytatódik

    #  A játék logikája a komment alatt folytatódik

    # 20 frame per másodpercre meghatározva
    clock.tick(1)

pygame.quit()
