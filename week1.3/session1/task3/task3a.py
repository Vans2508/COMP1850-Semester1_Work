# Week 1.3, Session 1: Task 3a

i = 0

while i < 20:
    i = i + 1 # we want it to be incremented each time so place it before the if statement
    if (i % 3) == 0: # we dont want non-multiples of 3 to be printed hence we continue the loop again
        continue    # goes to the next iteration of the loop
    print(i) # we want only the numbers not multiples of 3 to be printed so place after if statement

# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code