class Point():
    def __init__(self,x_cord,y_cord):
        self.x=x_cord
        self.y=y_cord
    def getpointx(self):
        return self.x
    def getpointy(self):
        return self.y
    def printme(self):
        print(str(self.x) + ' ' + str(self.y))
    

if __name__ == '__main__':
    mypoint=Point(1,2)
    hispoint=Point(24,6)

    hispoint.printme()
    print(mypoint.getpointx())
    print(mypoint is hispoint)