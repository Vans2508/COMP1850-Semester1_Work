
def listOf_integer_sum(lst_value): 
    ''' 
    This function takes a list of numbers as input and recursively goes through each number in the list and adding to a continuous sum and returning it
    ''' 
    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 