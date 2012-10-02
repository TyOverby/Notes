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

def t(theta, length = 1, deg=True):
    if not deg:
        theta = math.degrees(theta)

    if theta < -360 or theta > 360:
        theta = theta % 360
    if theta < 0:
        theta = 360 + theta

    x = length * (math.cos(math.radians(theta)))
    y = length * (math.sin(math.radians(theta)))

    return Vector2(x,y)
