"""Basic tests for the Rectangle class."""
import rect


rectangle = rect.Rectangle(4, 6)

print(rectangle.is_square()) 
print(rectangle.area()) #24
print(rectangle.perimeter())  #20

square = rect.Rectangle(5, 5)
print(square.is_square()) #True

print("Rectangle tests passed.")

import person

per = person.Person("Vanshita Swami","25/08/2008")
print(per.initials())
print(is_birthday())