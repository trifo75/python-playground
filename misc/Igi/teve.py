unneples=0
szomjusag = 0
valasz = 0
viztartalek = 100
energia = 100
tav = 0
uldozo = -20
#statusz csekk
q = 0
done = False
print("Elloptál egy tevét hogy átkelj a sivatagon és most üldöznek. Hogy megmenekülj át kell menj a sivatagon amire 100 pontnyi víz és 100 pontnyi energia áll rendelkezésedre. 100 Km-et kell megtegyél és a gyors haladás 20 Km-et jelent a lassú meg 10-et és pont ugyanennyi energiát és vizet is veszítessz velük")
while not done:

    valasz = input("A iszol \nB lassan haladsz \nC gyorsan haladsz \nD pihensz \nQ kilépsz \nE státusz csekk \n:")
    print ("a te válaszod:",valasz)
    if valasz.lower() == "e":

        print("víztartalék:",viztartalek,"energia:",energia,"táv",tav,"üldöző:",uldozo,"szomjuság:",szomjusag,"\n \n")
    else:

        uldozo += 10

        # ivás
        if valasz.lower() == "a":
            viztartalek -= 10
            energia += 10
            szomjusag = 0

        # lassan haladás
        elif valasz.lower() == "b":
            tav = tav + 10
            print("előrébb jutottál 10 Km-el")
            energia = energia - 10
            szomjusag += 10

        # gyorsan haladás
        elif valasz.lower() == "c":
            tav = tav + 20
            szomjusag += 20
            print("előrébb jutottál 20Km-el")
            energia = energia - 20

        # pihenés
        elif valasz.lower() == "d":
            energia += 20
            print("az energiád feljebb toltődött 20-szal")
        elif valasz.lower() == "q":
            done = True
        else:
            print("nem jót írtál")
            continue
    #összegzés
    if uldozo > tav:
        print("elkaptak")
        done = True
    if tav == 100:
        print ("megmenekültél")
        done = True
        unneples = 10
    if viztartalek == 0 or szomjusag > 30:
        print ("szomjan haltál")
        done = True

    if energia == 0:
        print("túlhajszoltad magad")
        done = True




#vége
if unneples == 10:
    print("gratulálok túljutottál")
else:
    print("ha gondolod próbáld újra")