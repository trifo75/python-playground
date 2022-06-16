
import random


# inditaskor beállítjuk, hogymekkora utat kell megtenni
# és hányszor tudunk inni
dist_ahead = random.randint(250,350)
drinks = random.randint(8,15)

# ilyen értékek között fogunk választani teljes sebesség és fél sebesség esetén
# (adott körben megtett km)
fullspeed_between = ( 45 , 62 )
halfspeed_between = ( 22 , 40 )

# ilyen értékekből fogunk választani az üldözők
# (adott körben megtett km)
enemy_speed_between = ( 20 , 40 )

refresh_one_drink = 40
refresh_one_sleep = 80

# megtett út (eleinte 0)
passed_km = 0
passed_km_enemy = -50

freshness = 100
hidration = 100

done = False


print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and out run the natives.")

while not done:
    print()
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    answer = input("Make your choice: ")
    if answer.upper() == "Q":
        done = True

    # ivás
    elif answer.upper() == "A":
        if drinks < 1 :
            print()
            print("Sorry, you are out of drinks. Be brave and hold up!")
        else:
            hidration += refresh_one_drink
            if hidration > 100:
                hidration = 100
            drinks -= 1


     # félsebesség előre
    elif answer.upper() == "B":
        passed_km += random.randint(halfspeed_between[0],halfspeed_between[1])
        freshness -= 20
        hidration -= 30
        passed_km_enemy += random.randint(enemy_speed_between[0],enemy_speed_between[1])

    # teljes sebesség
    elif answer.upper() == "C":
        passed_km += random.randint(fullspeed_between[0],fullspeed_between[1])
        freshness -= 47
        hidration -= 60
        passed_km_enemy += random.randint(enemy_speed_between[0],enemy_speed_between[1])

     # megáll aludni
    elif answer.upper() == "D":
        freshness = 100
        passed_km_enemy += random.randint(enemy_speed_between[0],enemy_speed_between[1])

    # státusz
    elif answer.upper() == "E":
        print()
        print("State:")
        print("You passed %d km out of %d km across the desert." % (passed_km, dist_ahead))
        print("Natives are %d km behind you" % (passed_km - passed_km_enemy))
        print("You have %d drinks in your canteen" % (drinks))
        print("Your freshness is {:.0f}% and hidration level is {:.0f}%".format(freshness, hidration))
        print()
    else:
        print("Your choice is not listed. Please choose from the menu.")

    print()
    # kiértékelés
    # ha utolértek, meghaltál
    if passed_km - passed_km_enemy <=0 :
        print("Oh, no! You chasers were too fast, you've been captured and now you are dead.")
        done = True
    elif hidration <= 0:
        print("Oh, no! You just died on thirst!")
        done = True
    elif freshness <= 0:
        print("Oh, no! You just died on tiredness!")
        done = True
    elif passed_km > dist_ahead:
        print("Congratulations! You've been corossing the desert successfully!")
        print("You are safe now, have a rest an enjoy life!")
        done = True




