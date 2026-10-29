# Week 1.5, Session 2: Task 2

# Write code here to create and print a Point object,
# then create and print a Circle object
import geometry

point = geometry.Point(1, 2.05)
print(point)
print(point.distance())
print(point.distance_to(geometry.Point(3.25, 2.0)))
print(point.distance_to(geometry.Point(1, 2.05)))

circle = geometry.Circle(5.0, geometry.Point(1, 2.05))
print(circle)
print(circle.area())
print(circle.perimeter())
print(circle.centre.distance())
print(circle.centre.distance_to(geometry.Point(3.25, 2.0)))