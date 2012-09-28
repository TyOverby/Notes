import re
import os
import math

class Vector3(object):
    def __init__(self, x, y, z):
        super(Vector3, self).__setattr__('x', x)
        super(Vector3, self).__setattr__('y', y)
        super(Vector3, self).__setattr__('z', z)

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+","+str(self.z)+">"

    def __repr__(self):
        return str(self)

    def __setattr__(self, *args):
        raise TypeError("Can't modify immutable vector")

    __delattr__ = __setattr__

    def __getitem__(self, key):
        if key is 0:
            return self.x
        elif key is 1:
            return self.y
        elif key is 2:
            return self.z
        elif key is "x":
            return self.x
        elif key is "y":
            return self.y
        elif key is "z":
            return self.z
    def __len__(self):
        return 3
