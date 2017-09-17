from swampy.TurtleWorld import *
import math
def polygon(penTool,vertices,radius):
    rotation_angle=360.0/vertices
    length=(2*radius*math.pi)/vertices
    lt(penTool,rotation_angle)
    fd(penTool,length)
    lt(penTool,rotation_angle*3)
    fd(penTool,radius)
    lt(penTool,rotation_angle*3)
    fd(penTool,radius)
def polyline(penTool,angle,length,vertices):
    for i in range(vertices):
        lt(penTool,angle)
        fd(penTool,length)
turtle=TurtleWorld()
pen=Turtle()
pen.delay=0.1
polygon(pen,8,50)
wait_for_user()
