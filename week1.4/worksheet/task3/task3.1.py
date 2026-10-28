def Multiplication(x,y):
    """
    This is a recursive function that multiplies two numbers by repeated addition
    """
    if y == 1:
        return x
    else:
        multiplication = x + (x * (y - 1))
        return multiplication

print(Multiplication(5,4)) #20
print(Multiplication(3,3)) #9