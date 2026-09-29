import math

# Object Oriented Programming Homework Assignment

# Task 1
class Line:
    def __init__(self, coor1, coor2):
        self.coord1 = coor1
        self.coord2 = coor2

    def distance(self):
        return math.sqrt((self.coord2[0] - self.coord1[0]) ** 2 + (self.coord2[1] - self.coord1[1]) ** 2)

    def slope(self):
        return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])

line = Line((8, 10), (3, 2))
print(line.distance())
print(line.slope())

# Task 2
class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())