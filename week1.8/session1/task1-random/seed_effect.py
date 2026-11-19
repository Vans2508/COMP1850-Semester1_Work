# See README.md for instructions on what to do this program

import random

random.seed(2)
#Intialises the random number generator so that the same value is printed each time for the same seed arguement
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

#It prints random integers between the value 1-100 three times 