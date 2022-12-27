import random
import pygame
import math

class Element():
    # objektum kezdeti koordinatai
    x_orig = 350
    y_orig = 200

    # objektum aktualis koordinatai
    xpos = x_orig
    ypos = y_orig

    # objektum iranya (fok) es sebessege (pixel/ciklus)
    speed = 0
    dir = 0

    # random valtoztassa-e a semesseget/iranyt a move() metodus
    randomize_speed = True
    randomize_dir = True

    # random valtoztatas hatarai
    max_dir_change = 2
    max_speed_change = .2

    def chg_dir_random():
        """
        irany megvaltoztatasa veletlenszeruen 
        max_dir_change erejeig, plusz vagy minusz iranyba
        """
        self.dir += random.random()*self.max_dir_chanege*2 - self.max_dir_change

