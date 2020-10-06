import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from math import degrees
from pymunk.vec2d import Vec2d

class Marble:
    image = pyglet.image.load('./res/marble1.png')
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    


    def __init__(self, space, id, newPosition):
        self.mass = 1
        self.radius = 30
        self.img = Marble.image
        self.anchor_x = self.img.width // 2
        self.anchor_y = self.img.height // 2

        circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
        self.body = pymunk.Body(self.mass, circle_moment)
        self.body.position = Vec2d(float(newPosition[0]), float(newPosition[1]))
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.id = id
        self.shape.elasticity = .5
        self.shape.friction = .68
        self.sprite = pyglet.sprite.Sprite(self.img, x=self.body.position[0], y=self.body.position[1])
        space.add(self.body, self.shape)

    def draw(self):
        if self.sprite !=None:
            self.sprite.draw()

    def update(self,space):
        #update sprite pos
        self.sprite.rotation = -degrees(self.body.angle)
        self.sprite.position = self.body.position
         
