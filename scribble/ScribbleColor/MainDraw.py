"""
ScribbleColor.py
Dillon Hussey
Project to allow user to draw with multiple colors from a toolbox
"""

import pyglet
import LineSegment, toolboxComponent
from pyglet.gl import GL_LINES, glBegin, glEnd, glVertex3f, glColor4f
window = pyglet.window.Window(1024,720,"ScribbleColor", resizable=False)


#global object for mode switching from draw, clearing, and erasing
isDraw = False
eraser = False
erasing = False
#Global variables for Segment Object
pointsList = []
holdSegment = None 
segmentColor = 0
segmentList = []

#creates toolbox and respective box coords + colors / function
toolbox =[]
toolbox = toolboxComponent.createToolbox(1024)



@window.event
def on_mouse_press(x, y, button, modifiers):
    
    #accessing global variables and enabling drawing by default. If clear or erase is clicked, then the 
    global isDrawing, holdSegment, pointsList, segmentColor, segmentList, eraser
    isDrawing = True

    if eraser == False:
        #Checks if cursor is in the toolbox, if so, checks which box, and selects that color / function (color, set erasing mode on, clear screen)
        if y < (1024/8):
            if x< (1024 * 6/8):
                segmentColor = int(x // (1024 / 8))
            else:
                if x > 1024 *7/8:
                    eraser = True
                else:
                    isDrawing = False
                    segmentList = []
                    


    
    #Starts a segment, clearing the points list, adding start point, and adding new segment to SegmentList
    if eraser == False:
        pointsList = []
        pointsList.append( (x,y) )
        holdSegment = LineSegment.LineSegment(pointsList, toolboxComponent.ColorComponent.colorList[segmentColor])
        segmentList.append(holdSegment)
    


# handle mouse dragging
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifier):
     global isDrawing, pointsList, eraser, segmentList, erasing
     
     #checks if mouse is erasing, if so then it goes through the process of searching for intersections and running the splitsegment method
     if eraser:
         for popindex, segment in enumerate(segmentList):
             for index, x1y1 in enumerate(segment.points):
                 x1, y1 = x1y1
                 if x1 > x-15 and x1 < x+15 and y1 > y-15 and y1 < y+15:
                     #segmentList.remove(segment)
                     erasing = True
                     segmentCopy = segmentList[popindex]
                     print(popindex)
                     segmentList.remove(popindex)
                     seg1, seg2 = LineSegment.splitSegment(segmentCopy, index)
                     
                     segmentList.append(seg1)
                     segmentList.append(seg2)
                     erasing = False
                     return
                     

     #ensures mouse is drawing to add point
     if isDrawing == True and eraser == False:
        pointsList.append( (x, y) )
     
   

# isDrawing =false, adds last point, adds Segment to Segment list as a new object with new points list
@window.event
def on_mouse_release(x, y, button, modifier):
     global isDrawing, pointsList, holdSegment, eraser
     
     if eraser == False:

        #only adds last point if mouse is drawing. (in clear and erase case it will not be)
        if isDrawing:
            pointsList.append((x, y))
            holdSegment.setPoints()
            isDrawing = False



@window.event #when this event is called, call this method (it is built into pyglet)
def on_draw():
     global segmentList, toolbox, erasing # colorList, white
     window.clear()
     # Begin Drawing
     if erasing == False:
        #run through each Segment and its respective points to draw lines
        glBegin(GL_LINES)
        if len(segmentList) > 0:
            for segments in segmentList:
                glColor4f( *segments.color)
                x1, y1 = segments.points[0]
                for x2, y2 in segments.points[1::]:
                    glVertex3f(x1, y1, 0)
                    glVertex3f(x2, y2, 0)
                    x1 = x2
                    y1 = y2
     glEnd()

    #color in toolbox
     for box in toolbox:
         glColor4f( *box.color)
         pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [box.x, box.y, box.x + box.width, box.y,box.x + box.width,   box.y + box.width, box.x, box.y + box.width]))
         

#pass means holding method
def update(dt):
    pass

#run main
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update,1.0/60)
    pyglet.app.run()

