import math

# Writing custom function to simulate test.testEqual
def testEqual(a,b):
    if a==b:
        return True
    else:
        return False


class Point():
    def __init__(self,intx,inty):
        self.x=intx
        self.y=inty
    def distacnefromorigin(self):
        dist=math.sqrt(math.pow(self.x,2)-math.pow(self.y,2))
        return dist
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy

point1=Point(2,3)
print(testEqual(point1.x,2))
        