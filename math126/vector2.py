import math

class Vector2(object):
    def __init__(self, x, y):
        def setval(name, value):
            super(Vector2, self).__setattr__(name, value)
        setval('x',x)
        setval('y',y)

        mag2 = self.x*self.x + self.y*self.y

        theta = math.degrees(math.atan2(self.y,self.x))
        if theta < -360 or theta > 360:
            theta = theta % 360
        if theta < 0:
            theta = 360 + theta

        setval('mag2',mag2)
        setval('mag', math.sqrt(mag2))
        setval('theta',theta)

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"

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
        elif key is "x":
            return self.x
        elif key is "y":
            return self.y

    def __len__(self):
        return 2

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)
    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self,other):
        return Vector2(self.x / other, self.y / other)


    def __neg__(self, other):
        return Vector2(-self.x, -self.y)

    def __or__(self, other):
        return self.magnitude
    def __ror__(self,other):
        return self.magnitude

    def dot(v1, v2):
        return v1.x*v2.x + v1.y*v2.y

    def to(self, other):
        return other-self

    __iadd__ = __setattr__
    __isub__ = __setattr__
    __imul__ = __setattr__
    __idiv__ = __setattr__
