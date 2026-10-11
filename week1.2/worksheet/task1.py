# Worksheet 1.2: Task 1 Solution
import sys

try:
    Grade = int(input(" Enter your integer grade "))
    if Grade >= 70 and Grade <= 100:
        print(f"{Grade} is a Distinction")
    elif Grade >= 40 and Grade <= 69:
        print(f"{Grade} is a Pass")
    elif Grade >= 0 and Grade <= 39:
        print(f"{Grade} is a Fail")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
except:
    sys.exit("Error: Grade must be an integer betwen 0 and 100")


