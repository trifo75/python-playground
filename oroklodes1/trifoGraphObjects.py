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
    max_dir_change = 4
    max_speed_change = .1

    # legyen basic szine
    color = (0, 255, 0)

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
    xsize = 20
    ysize = 20

    def draw(self,my_screen):
        posx = self.xpos - self.xsize / 2
        posy = self.ypos - self.ysize / 2
        pygame.draw.rect(my_screen,self.color,(posx,posy,self.xsize,self.ysize))

class Circle(Element):
    radius = 10

    def draw(self,my_screen):
        posx = self.xpos - self.radius
        posy = self.ypos - self.radius
        pygame.draw.circle(my_screen,self.color,(posx,posy),self.radius)

        