
# function implementation

def rectangle_area(length, width):  # define suitable input data
    """takes the length and width of the rectangle and outputs the area of it"""        
    # implement the function
    area = length * width
    return area             # return an appropriate value


# testing the function
print(f"Area is {rectangle_area(18, 7)}")   # provide suitable data matching your inputs

def Even_integer(value):
    """used to return the even valued integers from the list of integers from 0 to value"""
    Even_integer_list =[] #creating an empty list to add the even integers to
    for integer in range(value):
        if integer != 0 and integer % 2 == 0:
            Even_integer_list.append(integer)
        else:
            continue
    return Even_integer_list

value = int(input("Enter an integer value: "))
print(f"The even integers from 0 to {value} are {Even_integer(value)}")

