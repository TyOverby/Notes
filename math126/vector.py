import re
import os
import math

from vector2 import Vector2
from vector3 import Vector3

def v(*args):
    if len(args) is 2:
        return Vector2(args[0],args[1])
    elif len(args) is 3:
        return Vector3(args[0],args[1],args[2])
    else:
        raise TypeError("Two and three dimensional vectors are all that is supported")

