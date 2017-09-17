from swampy.TurtleWorld import *
import math
def arc(t, r, angle):
    """Draws the arc using the radius and angle of the of the circle.Also need the turtle object."""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
def circle(t, r):
    """Draws the circle take Radius as the argument and the Tutrtle object as the parameter."""
    arc(t,r,360)
def polygon(t, n, length):
    """Draws the polygon takes n as the number of edges and length as the length of each edge"""
    angle = 360.0 / n
    polyline(t, n, length, angle)
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
def arc2(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)
world=TurtleWorld()
bob=Turtle()
bob.delay=2
circle(bob,50)
wait_for_user()
