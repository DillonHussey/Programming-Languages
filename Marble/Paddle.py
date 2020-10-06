import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees, sin, pi
from pymunk.vec2d import Vec2d

class Paddle:


    def __init__(self, space, anchor, length):
        
        self.RsegBody = pymunk.Body(10, 10000)
        self.RsegBody.position = (anchor[0]+175, anchor[1])
        self.LsegBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.LsegBody.position = (anchor[0]-175, anchor[1])
        
        self.leftPaddle = pymunk.Segment(self.LsegBody, (anchor[0], anchor[1]), (anchor[0]+70, anchor[1]-40), 3)
        self.leftPaddle.friction = 1
        self.leftPaddle.elasticity = 1.5
       # self.Left = False
        #self.Lperiod=0
        self.rightPaddle = pymunk.Segment(self.RsegBody, (anchor[0], anchor[1]), (anchor[0]-70, anchor[1]-40), 3)
        pinBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        pinBody.position = (anchor[0]+165, anchor[1]-5)
        self.rightpin = pymunk.PinJoint(self.RsegBody, pinBody, (0,0), (anchor[0]+70, anchor[1]-40))
        #self.rightSpring = pymunk.DampedRotarySpring(self.RsegBody, pinBody, 0, 10, .5)
        self.rightPaddle.friction = 1
        self.rightPaddle.elasticity = 1.5
        #self.Right = False
        #self.Rperiod=0
        space.add(self.leftPaddle,self.rightPaddle, self.rightpin)


    def applyForceL(self):
        #self.Left=True

        pass
        
        """
        self.paddleCenterBody = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.paddleCenterBody.position= anchor

        self.paddleLimitB = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.paddleCenterBody.position= (anchor[0]-length/2, anchor[1])

        self.body = pymunk.Body(10, 1000)
        self.body.position = (anchor)
        self.pad = pymunk.Segment(self.body, (anchor[0]-10,anchor[1]+5),(50,50), 5)# (anchor[0]+20,anchor[1]-5), 5) 
        self.pad2 =pymunk.Segment(self.body, (anchor[0]-10,anchor[1]+5),(50,150), 5)# (anchor[0]+20,anchor[1]-5), 5) 
       
        self.rotationCenterJ = pymunk.PinJoint(self.body, self.paddleCenterBody,anchor, self.anchorCop)
        self.rotationLimitJ = pymunk.SlideJoint(self.body, self.paddleLimitB, self.paddleCenterBody.position, self.anchorCop,0, 25)
        space.add(self.pad, self.body, self.rotationCenterJ)



    def draw(self):
       # if self.sprite !=None:
            #self.sprite.draw()
        pass
"""
    def update(self,space, dt):
        #update sprite pos
       # if(self.Left and self.Lperiod>pi):
        #    self.Lperiod = self.Lperiod + dt
         #   print(self.Lperiod)
          #  self.leftPaddle.b = self.leftPaddle.b + 71*sin(self.Lperiod)
        #self.right
       # self.sprite.rotation = -degrees(self.body.angle)
        #self.sprite.position = self.body.position
        #elf.RsegBody.position 
        
        pass
