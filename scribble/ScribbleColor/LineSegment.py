import pyglet
import toolboxComponent
#from pyglet.gl import GL_LINES, glBegin, glEnd, glVertex3f

class LineSegment:

    #constructor for line segment
    def __init__(self, points, color):
        self.color = color
        self.points = points

    #copy new set of points and return new object (object will be reinitiated again on click so no need to clear data)
    def setPoints(self):
        pointsCopy = self.points.copy()
        colorCopy = self.color
        return LineSegment(pointsCopy, colorCopy)
    


    #this will split the segment into two segments and cut them off to the point where they are five pixels away from the cursor
def splitSegment(seg, index):
    #points1, points2 = seg.points
    x, y = seg.points[index]
    index1 = index
    x1, y1 = x, y
    #find where segment is five away running up (to index =0) in the points list to find first part of the split segment
    
    while (x1 >= x-3 and y1 >= y-3) and (x1 <= x+3 and y1 <= y+3):
        if index1 - 1 <= len(seg.points):
            x1, y1 = seg.points[index1-1]
            index1 -= 1
        else:
            break
        
    seg1 = LineSegment(seg.points[0:index1], seg.color)
    
    #find where segment is five away in the other direction of the points list to find second part of the split segment
    x1, y1 = x, y
    while (x1 >= x-3 and y1 >= y-3) and (x1 <= x+3 and y1 <= y+3):
        if index1 + 1 >= len(seg.points):
            x1, y1 = seg.points[index1+1]
            index1 += 1
        else:
            break
        
    seg2 = LineSegment(seg.points[index1::], seg.color)
    print(seg2.points[0])
    return seg1, seg2

