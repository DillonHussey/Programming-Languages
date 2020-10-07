import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import math
from pymunk.vec2d import Vec2d

ShapeList = {((5,775),(5,150),.8,1.0),
            ((650,675),(650,150),.8,1.0),
            ((5, 150),(155,75), .8, .68),
            ((650, 150),(650-145, 75), .5, .68),

            ((75, 275), (140, 225), 2, 1),
            ((655-75,275), (655-140, 225), 2, 1),    

            
            ((5,775), (50,805), 0.8, 1.0),
            ((650,675), (650-45,705), .8, 1.0),
            ((50,805), (650,805), .8, 1.0), 
            ((650, 805), (720, 700), 2, .1),
            ((720, 75), (720, 750), .8,1),


            #((650/4+50, 150), (650*3/4-50, 150), 3, .6),


            ((670,40), (705,40), 2.5, .001),

            #((327,580), 0, 2.1, .3),
            #((150,510), 0, 2.1, .3),
            #((504,510), 0, 2.1, .3)

                }

wallList = []

class Wall:
    image = pyglet.image.load('./res/marble1.png')
    

    
        
    def __init__(self, space, p):
        self.shape = segment_shape = pymunk.Segment(space.static_body, p[0], p[1], 2)
        self.shape.elasticity = p[2]
        self.shape.friction = p[3]
        space.add(self.shape)

        self.img = Wall.image

        leg1 = (p[0][0]- p[1][0])
        leg2 = (p[0][1]- p[1][1])
        self.img.width = ((p[0][0]- p[1][0])**2 +(p[0][1]- p[1][1])**2)**1/2
        self.img.height = (3)
        xc, yc= self.shape.body.position[0], self.shape.body.position[1]
      #  self.sprite = pyglet.sprite.Sprite(self.img,x=xc, y=yc)
      #  self.sprite.rotation = math.degrees(math.asin(leg2/leg1))

    def draw(self):
        if self.sprite !=None:
            self.sprite.draw()
    


def makeWalls(space):
    global wallList
    for x in ShapeList:
        seg = Wall(space,x)
        wallList.append(seg)

    


        

"""  This is for if i want to have moving objects
    def update(self,space):
        #update sprite pos
        self.sprite.rotation = -degrees(self.body.angle)
        self.sprite.position = self.body.position
"""
         
