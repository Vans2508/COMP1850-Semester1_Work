# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

import geometry

centre_point = geometry.Point(4.5, 7.2)
circle = geometry.Circle(centre_point, 3)

print(circle.centre.x_coordinate)  # 4.5
print(circle.centre.y_coordinate)  # 7.2
print(circle.radius)               # 3
print(circle.area())
print(circle.perimeter())

centre_another_point = geometry.Point(3.2,5.5)
circle1 = geometry.Circle(centre_another_point, 5)
print(circle1.centre.x_coordinate)
print(circle1.centre.y_coordinate)
print(circle1.radius)
print(circle1.area())
print(circle1.perimeter())