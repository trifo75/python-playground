import random
import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Element():

    def __init__(self, my_screen):

        # get screen geometry
        self.screen = my_screen
        self.screen_x, self.screen_y = my_screen.get_size()
        
        # objektum kezdeti koordinatai
        self.x_orig = self.screen_x / 2
        self.y_orig = self.screen_y / 2

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
        self.max_dir_change = 2
        self.max_speed_change = .1

        # legyen basic szine
        self.color = (0, 255, 0)



    def chg_dir_random(self):
        """
        irany megvaltoztatasa veletlenszeruen
        max_dir_change erejeig, plusz vagy minusz iranyba
        """
        self.dir = ( self.dir + random.random()*self.max_dir_change*2 - self.max_dir_change ) % 360

    def chg_speed_random(self):
        """
        sebesseg megvaltoztatasa veletlenszeruen
        max_speed_change erejeeig, + vagy - iranyba
        """
        self.speed += random.random()*self.max_speed_change*2 - self.max_speed_change

    # falat érés esetén
    def _bounce(self):
        self.dir = random.randrange(0,360)

    def _bouncewrap1(self):
        self.dir = random.randrange(0,4) * 90

    def _bouncewrap2(self):
        pass



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

        # számoljuk ki az elmozdulásokat
        delta_x = math.cos(dir_rad) * self.speed
        delta_y = math.sin(dir_rad) * self.speed

        # screen széléről visszapattanás (leesés gátlás)
        if self.xpos < 0:
            self.xpos = 0
            self._bounce()

        elif self.xpos > self.screen_x :
            self.xpos = self.screen_x
            self._bounce()

        else:
            self.xpos += delta_x

        if self.ypos < 0:
            self.ypos = 0
            self._bounce()

        elif self.ypos > self.screen_y :
            self.ypos = self.screen_y
            self._bounce()

        else:
            self.ypos += delta_y
        




            
        
class Rectangle(Element):

    def __init__(self,*args):
        super().__init__(*args)
        self.xsize = 20
        self.ysize = 20

    def draw(self,my_screen):
        posx = self.xpos - self.xsize / 2
        posy = self.ypos - self.ysize / 2
        pygame.draw.rect(self.screen,self.color,(posx,posy,self.xsize,self.ysize))
        pygame.draw.circle(self.screen,BLACK,(self.xpos,self.ypos),2)
        

class Circle(Element):

    def __init__(self,*args):
        super().__init__(*args)
        self.radius = 10

    def draw(self,my_screen):
        posx = self.xpos
        posy = self.ypos
        pygame.draw.circle(self.screen,self.color,(posx,posy),self.radius)
        pygame.draw.circle(self.screen,BLACK,(self.xpos,self.ypos),2)

        