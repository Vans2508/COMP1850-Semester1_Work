import random

# Get user to input how many random numbers they want
number = int(input("Enter how many random numbers you want: "))

# Generate this many random numbers
for i in range (number):
    print(random.randint(0,100))
# Write the random numbers to a file named random.txt, one number per line

print(random.random())