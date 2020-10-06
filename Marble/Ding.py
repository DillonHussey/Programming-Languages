import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
from pymunk.vec2d import Vec2d
import math

dings = {
            ((327,580), 0, 2.1, .3),
            ((150,510), 0, 2.1, .3),
            ((504,510), 0, 2.1, .3)

                }

dingList = []

class Ding:
    image = pyglet.image.load('./res/marble1.png')
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
     

    
        
    def __init__(self, space, x):
        self.shape = pymunk.Circle(space.static_body,15, x[0])
        self.shape.elasticity = x[2]
        self.shape.friction = x[3]
        space.add(self.shape)
        
        self.img = Ding.image
       
        

       # self.sprite = pyglet.sprite.Sprite(self.img, x=self.body.position[0], y=self.body.position[1])
        
       
    




    def draw(self):
        if self.sprite !=None:
            self.sprite.draw()
    
def makeDings(space):
    global dings
    for x in dings:
        seg = Ding(space,x)
        dingList.append(seg)


        

"""  This is for if i want to have moving objects
    def update(self,space):
        #update sprite pos
        self.sprite.rotation = -degrees(self.body.angle)
        self.sprite.position = self.body.position
"""
         
