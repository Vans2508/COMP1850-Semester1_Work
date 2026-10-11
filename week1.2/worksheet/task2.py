# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers 
numbers = read_numbers() 

if not numbers:
    sys.exit("Error: no numbers provided")
else:
    minimum_number = min(numbers)
    print(f"Minimum = {minimum_number}")
    
    maximum_number = max(numbers)
    print(f"Maximum = {maximum_number}")
    
    mean = sum(numbers)/len(numbers)
    print(f"Mean = {mean}")
    
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    mid = length // 2
    if length % 2 == 1:
        median = sorted_list[mid]
    else:
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2        
    print(f"Median = {median}")

