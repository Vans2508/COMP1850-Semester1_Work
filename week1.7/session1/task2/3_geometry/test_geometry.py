# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    # complete the implementation for
    # testing distance_to()
    assert p1.distance_to(p2) == 5.0
    
# Write test functions to test the __init__(), 
def test_circle_constructor():
    c = Circle(2.5, Point(2,4))
    assert c.radius == 2.5
    assert c.centre.x == 2
    assert c.centre,y == 4

import pytest 
# area() and perimeter() methods in Circle class
def test_area():
    assert Circle(2.5, Point(2,4)).area() == pytest.approx(19.6349540849)

def test_perimeter():
    assert Circle(2.5, Point(2,4)).perimeter() == pytest.approx(15.70796326)

# you can use the default value for centre coordinates
