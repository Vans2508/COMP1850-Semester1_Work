# Week 4, Session 2: 

# Given incomplete recursive function countdown with a docstring.
# Your task is to complete the function based on the details in the docstring.

def countdown(n):
    """
    This recursive function prints numbers from n down to 0.

    Args:
        n : int, positive integer representing the starting number.

    Returns:
        None, prints the countdown sequence from n to 0.
    """

    # Complete your code here
    # base case
    if n == 0:
        print(n, end=' ')
    # recursive case
    else:
        print(n, end=' ')
        countdown(n - 1)  # recursive call with n decremented by 1
    

# check if correct output is produced
countdown(30)    # 30 ... 0 (Note: each number is printed in a separate line)
countdown(5)     # 5 ... 0  (Note: each number in printed in a separate line)


# Once you have completed, your next task is to write an equivalent function that
# uses a loop.
def countdown_loop(n):
    """
    This function prints numbers from n down to 0 using a loop.

    Args:
        n : int, positive integer representing the starting number.
    Returns:
        None, prints the countdown sequence from n to 0.
    """
    for i in range(n, -1,-1):
        print(i,end=' ')
        if i == 0:
            break

# Test the loop-based function
countdown_loop(30)    # 30 ... 0 (Note: each number is printed in a separate line)
countdown_loop(5)     # 5 ... 0  (Note: each number in printed in a separate line)