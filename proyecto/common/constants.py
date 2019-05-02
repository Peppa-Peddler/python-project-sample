import math
from functools import reduce

class Punto:
    """Define coordinates field"""

    def __init__(self, coordinates = (0,0)):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def toTuple(self):
        return (self.x, self.y)

    def sum(*args):
        reduce(lambda a, b: Punto(a.x + b.x, a.y + b.y), args)


class Circulo:
    """radius is value, center is a tuple"""
    def __init__(self, radius = 100, center = (0,0), length = 8):
        self.radius = radius
        self.center = Punto(center)
        self.length = length

        self.points = []
        for i in range(length):
            coor = Punto(center)
            angle = 2*i*math.pi/self.length
            coor.x -= self.radius*math.cos(angle)
            coor.y -= self.radius*math.sin(angle)
            self.points.append(coor)

    def getPoints(self):
        return list(map(lambda P: P.toTuple(), self.points)) 
