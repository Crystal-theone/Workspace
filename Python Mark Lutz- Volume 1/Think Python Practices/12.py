from swampy.TurtleWorld import *
import math
def arc(t, r, angle):
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
def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)
def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw a sequence of three flowers, as shown in the book.
#move(bob, -100)
flower(bob, 3, 200.0, 45.0)

#move(bob, 100)
#flower(bob, 10, 40.0, 80.0)

#move(bob, 100)
#flower(bob, 20, 140.0, 20.0)

#die(bob)

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()