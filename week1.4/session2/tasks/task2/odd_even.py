# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """
    # Complete your code here
    Odd_count = 0 
    Even_count = 0
    for number in lstIntegers: #loop through the list of integers and check if each number is odd or even
        if number % 2 == 0:
            Even_count += 1
        else:
            Odd_count += 1
    return [Odd_count, Even_count]
    


# Check if correct output is produced
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]
