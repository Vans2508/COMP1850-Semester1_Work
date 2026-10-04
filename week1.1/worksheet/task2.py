"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
try:
    Monthly_savings = int(input('How much do you want to save every month? '))
    Annual_savings = Monthly_savings * 12
    print(f"The money you will save per year is £{Annual_savings}")
    Interest_earned = Annual_savings * 0.8
    Total_savings = Annual_savings + Interest_earned
    print(f"The total money you will have saved by the end of the year with interest is £{Total_savings:.2f}")
except:
    print(f"Invalid amount")
# Validate that they have entered an integer.
# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.
# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

