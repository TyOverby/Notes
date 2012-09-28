import re
import os
import math

class vector2:
    def __init__(self, x, y):
        self.x = x;
        self.wrapped = True
        self.y = y;

    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"

    def __repr__(self):
        return str(self)

    def __setattr__(self, name, value):
        try:
            if(self.wrapped):
                return
        except NameError:
            self.name = value


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

def vector_from_polar(theta, rho):
    if theta < -360 or theta > 360:
        theta = theta % 360
    if theta < 0:
        theta = 360 + theta

    return

def distance(vec1, vec2):
    deltax = vec1[0] - vec2[0]
    deltay = vec1[1] - vec2[1]
    deltaz = vec1[2] - vec2[2]

    dist_squared = deltax*deltax + deltay*deltay + deltaz*deltaz
    print "sqrt(" + str(dist_squared) + ")"
    return math.sqrt(dist_squared)

def get_vector(say="Input vector: "):
    text = raw_input(say)
    split = re.findall(r"-?\d+\.?\d*", text)
    if len(split) is not 3:
        print "Must contain 3 numbers seperated by a non-number"
        os._exit(1)
    return (float(split[0]), float(split[1]), float(split[2]))


def distance_sub(vec1=None):
    if vec1 == None:
        print distance(get_vector("Enter First Vector: "), get_vector("Enter Second Vector: "))

def main_switch():
    text = raw_input("Enter a command: ")
    if "dist" in text:
        distance_sub();
        if "+" in text:
            print "\nnext:\n"
            main_switch(text)

    else:
        print "Command not found.  Quitting"
        os._exit(1)

#main_switch()
#os._exit(0)
