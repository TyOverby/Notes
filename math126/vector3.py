import re
import os
import math

class Vector3(object):
    def __init__(self, x, y, z):
        super(Vector3, self).__setattr__('x', x)
        super(Vector3, self).__setattr__('y', y)
        super(Vector3, self).__setattr__('z', z)

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">"

    def __repr__(self):
        return str(self)

    def __setattr__(self, *args):
        raise TypeError("Can't modify immutable vector")

    def __getattr__(self, name):
        if name in ["magnitude", "mag", "rho"]:
            return math.sqrt(self.mag2)
        elif name is "mag2":
            return self.x*self.x + self.y*self.y + self.z*self.z
        else:
            return super(Vector2, self).__getattr__(name)

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


    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self,other):
        return Vector3(self.x / other, self.y / other, self.z / other)


    def __neg__(self, other):
        return Vector3(-self.x, -self.y, -self.z)

    def __or__(self, other):
        return self.magnitude
    def __ror__(self,other):
        return self.magnitude

    def dot(v1, v2):
        return v1.x*v2.x + v1.y*v2.y + v1.z*v2.z

    def cross(v1, v2):
        return Vector3(v1.y * v2.z - v1.z * v2.y,    v1.z * v2.x - v1.x * v2.z,    v1.x * v2.y - v1.y*v2.x)

    def to(self, other):
        return other-self

    __iadd__ = __setattr__
    __isub__ = __setattr__
    __imul__ = __setattr__
    __idiv__ = __setattr__
