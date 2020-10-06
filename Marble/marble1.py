import pyglet
import pymunk 
import Marble
from pymunk.pyglet_util import DrawOptions
from math import degrees
from Marble import Marble

#window and space setup
window = pyglet.window.Window(1400,720, "DK", resizable = False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
sprites = []
batch = pyglet.graphics.Batch()


#model =

"""
#circle param
mass = 1
radius = 30
marble_img = pyglet.image.load('./res/marble1.png')
marble_img.anchor_x = marble_img.width // 2
marble_img.anchor_y = marble_img.height // 2
"""

# dynamic: can be affected by gravity, high computing power

# kinematic: not affected by gravity, but can move, med computing power

# static: not moving or affected by gravity

segment_shape = pymunk.Segment(space.static_body, (0,0), (800,40), 2)
segment_shape.body.position = 500, 400
segment_shape.elasticity = 1.0
segment_shape.friction = .03
space.add(segment_shape)


segment_shape = pymunk.Segment(space.static_body, (0,60), (800,0), 2)
segment_shape.body.position = 100, 100
segment_shape.elasticity = .8
segment_shape.friction = 1.0
space.add(segment_shape)



@window.event
def on_mouse_press(x,y,button, modifier):
    #add a marble
    marbleBody = Marble(space, 100, (x,y))
    sprites.append(newSprite)
    space.add(circle_body, circle_shape)
   
    """# add circles
    circle_moment = pymunk.moment_for_circle(mass, 0,radius)
    circle_body = pymunk.Body(mass, circle_moment)
    circle_body.position = x,y
    circle_shape = pymunk.Circle(circle_body, radius)
    circle_shape.elasticity = .68 #.68
    circle_shape.friction = .68
    sprites.append(pyglet.sprite.Sprite(marble_img, *circle_body.position, batch = batch))

    space.add(circle_body, circle_shape)
"""




@window.event
def on_draw():
        window.clear()
        space.debug_draw(options)
        
        #handle marble drawing
        for locMarble in marbles
            locMarble.draw



def update(dt):
    space.step(dt)
    
    for locMarble in marbles:
        locMarble.update(space)
    
    
    for index, sprite, in enumerate(sprites):
        #update the sprite position
        sprite.position = space.bodies[index].position
        sprite.rotation = -degrees(space.bodies[index].angle)
        sprite.position = space.bodies[index].position
        if sprite.position[1] < -2:
            sprites.remove(sprite)
           

    #remove shapes once they are out of view
    for shape in space.shapes:
        if shape.body.position.y < -2:
            space.remove(shape.body, shape)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()


