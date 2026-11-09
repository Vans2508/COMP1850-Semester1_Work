# Week 1.7, Session 1: Task 2 - unit test for comfort_level() 

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(12.3) == "COLD"
    assert comfort_level(-1.5) == "COLD"

def test_hot():
    assert comfort_level(33) == "HOT"
    assert comfort_level(25.0) == "HOT"

def test_ok():
    assert comfort_level ( 17.0) == "OK"
    assert comfort_level (23.4) == "OK"

print(test_cold())
print(test_hot())  
print(test_ok())