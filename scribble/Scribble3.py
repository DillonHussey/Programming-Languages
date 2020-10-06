import pyglet
from pyglet.gl import GL_LINES, glBegin, glEnd, glVertex3f
window = pyglet.window.Window(1024,720,"Scribble3", resizable=False)

#Drawing Vectors
drawing_vec = []
isDraw = False
startPoint = None

@window.event
def on_mouse_press(x, y, button, modifiers):
    global isDrawing, startPoint
    isDrawing = True
    startPoint = (x, y)

# handle mouse dragging
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifier):
     global isDrawing, startPoint, drawing_vec
     
     if isDrawing == True:
         drawing_vec.append((startPoint[0], startPoint[1], x, y))
         startPoint = (x,y)
    

@window.event
def on_mouse_release(x, y, button, modifier):
     global isDrawing, startPoint, drawing_vec
     isDrawing = False
     drawing_vec.append((startPoint[0], startPoint[1], x, y))



@window.event #when this event is called, call this method (it is built into pyglet)
def on_draw():
    window.clear()
    # Begin Drawing
    glBegin(GL_LINES)
    # create a line w/ x,y,z
    global drawing_vec
    if not drawing_vec == None:
        for bstart, bend, estart, eend in drawing_vec:
            glVertex3f(bstart, bend, 0.0)
            glVertex3f(estart, eend, 0.0)
    glEnd()





#pass means holding method
def update(dt):
    pass



if __name__ == "__main__":
    pyglet.clock.schedule_interval(update,1.0/60)
    pyglet.app.run()

