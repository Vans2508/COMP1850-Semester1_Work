# Week 4, Session 1

# You are given the function mystery_func. 
# Inspect the code in the function
# Your task is to write a corresponding docstring
# - what the function does 
# - what is the input data and type
# - what is the return value and type


# function implementation

def mystery_func(string):
    """Finds the number of uppercase and lowercase characters in the inputed string contains
    Args: The string to check for the number of uppercase and lowercase characters 
    Return: The number of uppercase characters in the string
            The number of lowercase characters in the string
    """
    
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1
    return (upper, lower)


# testing

print(mystery_func("abc"))
print(mystery_func("The quick Brown Fox!"))
print(mystery_func("012345"))
print(mystery_func("ABC"))


# Can you predict the output of the following lines of code?
# Uncomment the lines of code one by one and run the program
# to see if you are right?

print(mystery_func("X")) #has only one uppercase letter so returns (1,0)
print(mystery_func("[2, 3]")) #is not a string so returns (0,0)
