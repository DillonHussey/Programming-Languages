import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
from pymunk.vec2d import Vec2d
import math
#list of dings
dings = {
            ((327,580), 0, 2.1, .3),
            ((150,510), 0, 2.1, .3),
            ((504,510), 0, 2.1, .3)

                }

dingList = []

class Ding:
    image = pyglet.image.load('./res/marble2.png')
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
     
        
    def __init__(self, space, pos):

        self.shape = pymunk.Circle(space.static_body,15, pos[0])
        self.shape.elasticity = pos[2]
        self.shape.friction = pos[3]
        self.shape.id = 200
        space.add(self.shape)
        
        self.img = Ding.image
       
        self.sprite = pyglet.sprite.Sprite(self.img, x=pos[0][0], y=pos[0][1])
        
       
    




    def draw(self):
        if self.sprite !=None:
            self.sprite.draw()
    
def makeDings(space):
    global dings
    for x in dings:
        seg = Ding(space,x)
        dingList.append(seg)


         
