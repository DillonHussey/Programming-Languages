"""
wordList = '1,3,2,4,5,3,2,1,4,3,2'.split(',')

def examplesOf(wList):
    wDict = {char:0 for char in wList}
    
    for char in wList:
        wDict[char] +=1
    
    return wDict

examplesOf(wordList)
"""

class Animal():

    def __init__(self, herd, legs):
        self.legs = legs
        self.herd = herd
    
    def getLegs(self):
        return self.herd * self.legs
    
class Cow(Animal):
    def __init__(self, num):
        self.legs = 4
        self.herd = num

        
class Chicken(Animal):
    def __init__(self, num):
        self.legs = 2
        self.herd = num

class Farm():

    def __init__(self, chickNum, CowNum):
        self.Chicken = Chicken(chickNum)
        self.Cow = Cow(CowNum)
        
    def getTotalLegs(self):
        return self.Chicken.getLegs() + self.Cow.getLegs()


myFarm  = Farm(20,50)
print(myFarm.getTotalLegs())