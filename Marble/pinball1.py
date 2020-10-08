import pyglet
import pymunk 
import Marble
import Wall
import Ding
import math
import random
from pymunk.pyglet_util import DrawOptions
from pyglet import image
from pyglet.window import key
from pymunk.vec2d import Vec2d
from score import score
from Marble import Marble

c=0 # ball counter
#window and space setup
window = pyglet.window.Window(720,810, "Baby Yoda Pinball", resizable = False)
options = DrawOptions()
space = pymunk.Space()
space.gravity = 0, -1000
active = False
marbles = []
walls = []
yodaimg = pyglet.image.load('./res/babyYoda.png')
yoda = pyglet.sprite.Sprite(yodaimg, 10,10)
Wall.makeWalls(space)
Ding.makeDings(space)
#setting up score
playerScore = 0
scoreBoard = score(playerScore)


#Making the Paddles, and connected spring
#Left Paddle
rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC) 
rotation_center_body.position = (650/4, 175+30)
body = pymunk.Body(10, 10000) 
body.position = (650/4, 175+30)
leftPaddle = pymunk.Segment(body, (120, -50), (0.0, 0.0), 7.0)
leftPaddle.id = 200
leftPaddle.elasticity = 2
rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0)) 
leftSpring = pymunk.DampedRotarySpring(body, rotation_center_body, 0, 500000, 100000)

#Right Paddle
rotation_center_body2 = pymunk.Body(body_type = pymunk.Body.STATIC) 
rotation_center_body2.position = (650*3/4, 175+30)
body2 = pymunk.Body(10, 10000) 
body2.position = (650*3/4, 175+30)
rightPaddle = pymunk.Segment(body2, (-120, -50), (0.0, 0.0), 7.0)
rightPaddle.id = 200
rightPaddle.elasticity = 2
rotation_center_jointR = pymunk.PinJoint(body2, rotation_center_body2, (0,0), (0,0))
rightSpring = pymunk.DampedRotarySpring(rotation_center_body2, body2, 0, 500000, 100000)

#add bodies to space
space.add(leftSpring, leftPaddle, body, rotation_center_joint, rightPaddle, body2,rotation_center_jointR, rightSpring )



#Collision detecting. Only adds if ball hits paddles, bottom bumpers or 'dingers' physics with dingers seems to make this not work consistently
def coll_separate(arbitor, space, data):
    if len(arbitor.shapes) > 1:
        if arbitor.shapes[0].id == 100 and \
            arbitor.shapes[1].id == 200:
                scoreBoard.updateScoreDiff(10)
             #blipSound.play()


handler = space.add_default_collision_handler()
handler.separate = coll_separate


@window.event
def on_key_press(symbol, modifier):
    global c, window, marbles, active
    #add a marble, but makes sure the other marble are not active
    if(symbol == key.SPACE and active==False):
        c = c+1
        active = True
        marbleBody = Marble(space, 100, (700,random.randint(400, 700)))
        marbles.append(marbleBody)
    #move left and right paddles
    elif(symbol == key.LEFT):
        body.apply_impulse_at_local_point(Vec2d.unit() * 800, (body.position.x, body.position.y ))
    elif(symbol == key.RIGHT):
        body2.apply_impulse_at_local_point(Vec2d.unit() * -300, (body2.position.x, body2.position.y ))



@window.event
def on_draw():
        global yoda, leftSpring
        window.clear()
        #draw brackground
        yoda.draw()
        space.debug_draw(options)
        #handles drawing walls
        for seg in Wall.wallList:
            seg.draw()
        #handle drawing dings
        for dings in Ding.dingList:
            dings.draw()
        #handle marble drawing
        for locMarble in marbles:
            locMarble.draw()
        
        #Display Score
        label = pyglet.text.Label(str(scoreBoard.numScore),font_name='Times New Roman',font_size=36,x=window.width//5, y=window.height*4//5, anchor_x = 'center', anchor_y= 'center')#, anchor_x='center', anchor_y='center')
        label.draw()

        



def update(dt):
    global c, active
    space.step(dt)
    
    #update all the marbles location
    for locMarble in marbles:
        locMarble.update(space)

    #remove shapes once they are out of view and exits if ball is over three
    for shape in space.shapes:
        if shape.body.position.y < -30:
            active = False
            if(c>=3):
                window.close()
            space.remove(shape.body, shape)
            


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1.0/60.0)
    pyglet.app.run()


