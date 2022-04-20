toolbox = []

class ToolboxComponent:

    def __init__(self, x, y, width1):
         self.x = x
         self.y = y
         self.width = width1
         self.height = width1


class ColorComponent(ToolboxComponent):

     
     #colors
     red = (1, 0.2, 0.2,0.2)
     green = (.2, 1, .2, .2)
     blue = (.1, .6, 1,0.2)
     yellow = (.95, .95, .3,1)
     teal = (.2, .7, .7,1)
     pink = (.9, .3, .7,1)
     grey = (.5,.5,.5,1)
     white = (1,1,1,1)

     colorList = [red, green, blue, yellow, teal, pink, grey]
     
    #intialize new ColorComponent object as a using toolbox constructor
     def __init__(self, x, y, width, height, color):
         colorList = ColorComponent.colorList
         #for some reason I kept getting errors so i could not properly utilize super()__init__ method for actual polymorphism
         self.x = x
         self.y = y
         self.width = width
         self.height = width
         self.color = colorList[color]

class ClearComponent(ToolboxComponent):
    grey = (.5, .5, .5, 1)
    def __init__(self, x, y, width, height):
         self.x = x
         self.y = y
         self.width = width
         self.height = width
         self.color = ColorComponent.grey


class EraserComponent(ToolboxComponent):
    darkgrey = (.3, .3, .3, 1)
    def __init__(self, x, y, width, height):
         self.x = x
         self.y = y
         self.width = width
         self.height = width
         self.color = ColorComponent.grey
        

    
def createToolbox(windowWidth):
        global toolbox
        for x in range(8):
            if x<6:
                colorBox = ColorComponent(windowWidth * x / 8, 0, windowWidth/8, windowWidth/8, x)
                toolbox.append(colorBox)
            elif x == 6:
                clearbox = ClearComponent(windowWidth * x / 8, 0, windowWidth/8, windowWidth/8)
                toolbox.append(clearbox)
            elif x == 7:
                pass
        return toolbox

        
