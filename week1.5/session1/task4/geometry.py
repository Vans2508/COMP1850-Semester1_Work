# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""
import math
# Copy Point class definition here
class Point:
    """
    A Point in 2D space.
    """

        # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def distance(self):
        return math.hypot(self.x_coordinate,self.y_coordinate)
        
    def distance_to(self,another_x, another_y):
        self.another_x = another_x
        self.another_y = another_y
        distance = math.sqrt((self.x_coordinate - self.another_x)) + math.sqrt((self.y_coordinate - self.another_y))
        return distance


# Add a definition for a Circle class here, giving it
class Circle:
    #  - A constructor that creates fields to represent the centre & radius
    #    of a circle (assume centre is represented as a Point object)
    def __init__(self,centre,radius):
        self.centre = centre
        self.radius = radius 
    #  - A method area(), returning the area of the circle
    def area(self):
        area = math.pi * self.radius**2
        return area
    #  - A method perimeter(), returning the perimeter of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius


# Don't add any testing code to this file!
