from swampy.TurtleWorld import *
import math

def drawFlower(penTool,num_of_petals,petal_radius,petal_angle):
    petal_angle_offset=360.0/num_of_petals
    for i in range(num_of_petals):
        drawPetal(penTool,petal_radius,petal_angle)
        lt(penTool,petal_angle_offset)
        break
def drawPetal(penTool,radius,angle):
    drawArc(penTool,radius,angle)
    lt(penTool,180-angle)
    drawArc(penTool,radius,angle)
    lt(penTool,180-angle)
    #rt(penTool,angle*2.0)
def drawArc(penTool,radius,angle):
    arc_length=2*math.pi*(angle/360.0)*radius
    num_of_vertices=int(arc_length/2.0)+1
    step_angle=angle/num_of_vertices
    step_length=arc_length/num_of_vertices
    lt(penTool,step_angle/2.0)
    polyLine(penTool,num_of_vertices,step_angle,step_length)
    rt(penTool,step_angle/2.0)
def polyLine(penTool,vertices,angle,length):
    for i in range(vertices):
        lt(penTool,angle)
        fd(penTool,length)

world=TurtleWorld()
penTool=Turtle()
penTool.delay=0.05
drawFlower(penTool,3,123,45.0)
wait_for_user()