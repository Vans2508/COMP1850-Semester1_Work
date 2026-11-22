import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
    num = int(input("Enter a number "))

    for i in range (num):
        print(f" {random.choice(names)}")
# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line


random.choice([k for k in range(3,21,2)])