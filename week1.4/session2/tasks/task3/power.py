# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.


def power(x, n):
    # complete your code here
    # base case
    if n == 0:
        return 1
    # recursive case
    else:
        return x * power(x, n - 1) #recursive call with n decremented by 1 to calculate x raised to the power of n-1 and then multiply it by x to get the final result of x raised to the power of n.


# Once completed, make at least two function calls to test the power function
print(power(2, 3))  # Output: 8
print(power(5, 2))  # Output: 25
print(power(3, 4))  # Output: 81
print(power(10, 0))  # Output: 1
print(power(2, 5))  # Output: 32

def power_loop(x, n):
    """
    This function calculates x raised to the power of n using a loop.

    Args:
        x (int or float): The base number.
        n (int): The exponent (non-negative integer).

    Returns:
        int or float: The result of x raised to the power of n.
    """
    # complete your code here
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result *= x  # multiply the result by x for n times
    return result

#test the loop-based function
print(power_loop(2, 3))  # Output: 8
print(power_loop(5, 2))  # Output: 25
print(power_loop(3, 4))  # Output: 81