# Week 1.5, Session 1: Task 3
import math 
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
    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
dot = Point(4.5, 7.2)
print(dot.x_coordinate, dot.y_coordinate)
print(dot.distance())
print(dot.distance_to(2.4,6.3))