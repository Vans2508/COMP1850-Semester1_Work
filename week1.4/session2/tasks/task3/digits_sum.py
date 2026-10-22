# Week 4, Session 2: Task 4

# Given incomplete recursive function digits_sum with a docstring,
# your task is to complete the function based on the description


def digits_sum(number):
    """
    This recursive function calculates the sum of digits of a given positive
    integer. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
    For simplisity, ignore the case when number is not an integer or
    not a positive integer.

    Args:
        number (int): The input is a positive integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    # complete your code here
    # base case
    if number == 0:
        return 0
    else:
        # recursive case
        return number % 10 + digits_sum(number // 10)  # add the last digit to the sum of the remaining digits using integer division to remove the last digit by first getting the last digit using modulus operator and then calling the function recursively with the remaining digits obtained by integer division by 10.
    


# check if correct output is produced
print(digits_sum(987))  # Output: 24
print(digits_sum(12345))  # Output: 15


# Once completed, your next task is to write an equivalent function that uses loops.

def digits_sum_loop(number):
    """
    This function calculates the sum of digits of a given positive integer
    using a loop. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
    For simplisity, ignore the case when number is not an integer or
    not a positive integer.

    Args:
        number (int): The input is a positive integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    # complete your code here
    total_sum = 0
    while number > 0:
        total_sum += number % 10  # add the last digit to the total sum using modulus operator to get the last digit and then add it to the total sum
        number //= 10  # remove the last digit from the number using integer division by 10
    return total_sum

#test the loop-based function
print(digits_sum_loop(987))  # Output: 24
print(digits_sum_loop(12345))  # Output: 15