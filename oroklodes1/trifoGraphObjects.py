import random
import pygame
import math

class Element():

    self.tibi = 6
    


    def __init__(self):
        # objektum kezdeti koordinatai
        self.x_orig = 350
        self.y_orig = 200

        # objektum aktualis koordinatai
        self.xpos = self.x_orig
        self.ypos = self.y_orig

        # objektum iranya (fok) es sebessege (pixel/ciklus)
        self.speed = 0
        self.dir = 0

        # random valtoztassa-e a semesseget/iranyt a move() metodus
        self.randomize_speed = True
        self.randomize_dir = True

        # random valtoztatas hatarai
        self.max_dir_change = 4
        self.max_speed_change = .1

        # legyen basic szine
        self.color = (0, 255, 0)

    def chg_dir_random(self):
        """
        irany megvaltoztatasa veletlenszeruen
        max_dir_change erejeig, plusz vagy minusz iranyba
        """
        self.dir += random.random()*self.max_dir_change*2 - self.max_dir_change

    def chg_speed_random(self):
        """
        sebesseg megvaltoztatasa veletlenszeruen
        max_speed_change erejeeig, + vagy - iranyba
        """
        self.speed += random.random()*self.max_speed_change*2 - self.max_speed_change

    def move(self):
        """
        mozgas egy lepessel sebesseg es irany alapjan
        ha kell, elotte randomizalunk
        """
        if self.randomize_speed :
            self.chg_speed_random()

        if self.randomize_dir :
            self.chg_dir_random()

        # váltsuk a fokot radiánba 
        dir_rad = self.dir / 180 * math.pi

        # számoljuk ki az elmozdulásokat és mozduljunk
        self.xpos += math.cos(dir_rad) * self.speed
        self.ypos += math.sin(dir_rad) * self.speed
        
class Rectangle(Element):

    def __init__(self):
        Element.__init__(self)
        self.xsize = 20
        self.ysize = 20

    def draw(self,my_screen):
        posx = self.xpos - self.xsize / 2
        posy = self.ypos - self.ysize / 2
        pygame.draw.rect(my_screen,self.color,(posx,posy,self.xsize,self.ysize))

class Circle(Element):

    def __init__(self):
        Element.__init__(self)
        self.radius = 10

    def draw(self,my_screen):
        posx = self.xpos - self.radius
        posy = self.ypos - self.radius
        pygame.draw.circle(my_screen,self.color,(posx,posy),self.radius)

        