import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import math
from pymunk.vec2d import Vec2d

#data for each shape
ShapeList = {((5,775),(5,150),.8,1.0,0),
            ((650,675),(650,150),.8,1.0,0),
            ((5, 150),(155,75), .8, .68,0),
            ((650, 150),(650-145, 75), .5, .68,0),

            ((70, 275), (140, 225), 2, 1,200),
            ((655-70,275), (655-140, 225), 2, 1,200),    

            
            ((50,805),(5,775) , 0.8, 1.0,0),
            ((650-45,705),(650,675), .8, 1.0,0),
            ((50,805), (650,805), .8, 1.0,0), 
            ((650, 805), (720, 700), 2, .1,0),
            ((720, 75), (720, 750), .8,1,0),


           

            ((670,40), (705,40), 2.5, .001,0),

           
                }

wallList = []

class Wall:
    #loads image and sets anchor
    image = pyglet.image.load('./res/background.png')
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

    
        
    def __init__(self, space, p):
        #shape data
        self.shape = segment_shape = pymunk.Segment(space.static_body, p[0], p[1], 2)
        self.shape.elasticity = p[2]
        self.shape.friction = p[3]
        space.add(self.shape)

        self.img = Wall.image
        self.shape.id = p[4]
        leg1 = (p[1][0]- p[0][0])
        leg2 = (p[1][1]- p[0][1])
        #makes sprite centered at the average of endpoints
        self.sprite = pyglet.sprite.Sprite(self.img,x=(p[0][0]+p[1][0])/2, y=(p[0][1]+p[1][1])/2)#float(xc), y=float(yc))
        #sets scale to segment length (pythag theorem) / image width
        self.sprite.scale_x =(((leg1**2 + leg2**2) **.5) /(self.sprite.width))
        self.sprite.scale_y = .05
        #use trig to find angle to rotate sprite
        angle = math.degrees(math.acos(leg1 / (leg1**2 + leg2**2)**.5 ))
        self.sprite.rotation = angle


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
         
