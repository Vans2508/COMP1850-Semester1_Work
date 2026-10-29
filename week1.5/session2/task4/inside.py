# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry

# Create a circle with radius 5 and centre at (0, 0)
circle = geometry.Circle(5, geometry.Point(0, 0))

# Create a point at (5, 2.05)
point = geometry.Point(5, 0)

# Check if the point is inside the circle
if point in circle:
    print("The point is inside the circle.")
else:
    print("The point is not inside the circle.")