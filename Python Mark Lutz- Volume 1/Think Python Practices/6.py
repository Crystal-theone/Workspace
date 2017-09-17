from swampy.TurtleWorld import *

def drawSquare(obj,length):
    for i in range(4):
        fd(obj,length)
        lt(obj)
def drawPolygon(obj,length,vertices,angle=360):
    turn=angle/vertices
    for i in range(vertices):
        fd(obj,length)
        lt(obj,turn)
def drawCircle(obj,radius):
    fd(obj,radius)
    lt(obj)
    drawPolygon(obj,1,360)
def drawGeneralCircle(obj,radius,angle):
    fd(obj,radius)
    lt(obj)
    drawPolygon(obj,1,120,angle)
world = TurtleWorld()
bob = Turtle()
print bob
#drawSquare(bob,120)
#drawPolygon(bob,100,6)
bob.delay=0.001
drawGeneralCircle(bob,100,120)
wait_for_user()