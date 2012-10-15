import re
import os
import math

from vector2 import Vector2
from vector3 import Vector3

def v(*args):
    if len(args) is 2:
        return Vector2(float(args[0]),float(args[1]))
    elif len(args) is 3:
        return Vector3(float(args[0]),float(args[1]),float(args[2]))
    else:
        raise TypeError("Two and three dimensional vectors are all that is supported")

def t(rho=1, theta=0, deg=False):

    if not deg:
        theta = math.degrees(theta)

    if theta < -360 or theta > 360:
        theta = theta % 360
    if theta < 0:
        theta = 360 + theta

    x = rho * (math.cos(math.radians(theta)))
    y = rho * (math.sin(math.radians(theta)))

    return Vector2(x,y)
