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
from datetime import date

per = person.Person("Vanshita Swami", date(2008, 8, 25))
print(per.initials())
print(per.is_birthday())
