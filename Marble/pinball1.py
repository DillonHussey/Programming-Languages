import pyglet
import pymunk 
import Marble
import Wall
import Ding
import random
from pymunk.pyglet_util import DrawOptions
from pyglet import image
from pyglet.window import key
from pymunk.vec2d import Vec2d
from math import degrees
from Marble import Marble
from Paddle import Paddle


c=0
#window and space setup
window = pyglet.window.Window(720,810, "DK", resizable = False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
# sprites = []
marbles = []
walls = []
yodaimg = pyglet.image.load('./res/babyYoda.png')
yoda = pyglet.sprite.Sprite(yodaimg, 10,10)
Wall.makeWalls(space)
Ding.makeDings(space)
pad1 = Paddle(space, (650/4, 100), 30)



@window.event
def on_mouse_press(x,y,button, modifier):
    global marbles
    #add a marble
    #marbleBody = Marble(space, 100, (x,y))
    #marbles.append(marbleBody)
    #pad1.applyForceL()

    # sprites.append(marbleBody.sprite)
    #space.add(marbleBody.body, marbleBody.shape)
    
    #use pin joint, damped rotary spring
@window.event
def on_key_press(symbol, modifier):
    global c, window, marbles
    
    if(symbol == key.SPACE):
        #add a marble
        if(c>=3):
            window.close()
        c = c+1
        marbleBody = Marble(space, 100, (700,random.randint(400, 700)))
        marbles.append(marbleBody)
        #pad1.applyForceL()
    elif(symbol == key.UP):
        pass
        for marble in marbles:
            x = marble.body.position.x
            y= marble.body.position.y
            if(x>650/4 and x<650*3/4 and y<230 and y>10):
                marble.body.velocity = marble.body.velocity * -1.1
        
    # sprites.append(marbleBody.sprite)
    #space.add(marbleBody.body, marbleBody.shape)



@window.event
def on_draw():
        global yoda
        window.clear()
        
        space.debug_draw(options)
        #yoda.draw()
       # pad1.draw()
        #handle marble drawing
        for locMarble in marbles:
            
            locMarble.draw()

        



def update(dt):
    pad1.update(space, dt)
    space.step(dt)
    
    

   # pad1.update(space)
    
    #update all the marbles location
    for locMarble in marbles:
        locMarble.update(space)

    #remove shapes once they are out of view
    for shape in space.shapes:
        if shape.body.position.y < -20:
            space.remove(shape.body, shape)
            
            



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()


