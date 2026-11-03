# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        if type(width) is not int:
            raise TypeError("Width must be an integer")

        if type(height) is not int:
            raise TypeError("Height must be an integer")

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        if height <= 0:
            raise ValueError("Height must be greater than 0")

        self.width = width
        self.height = height
    
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        """
        Returns True if this Rectangle is a square, False otherwise.
        """
        return self.width == self.height
    def area(self):
        """
        Returns the area of this Rectangle.
        """
        return self.width * self.height
    def perimeter(self):
        """
        Returns the perimeter of this Rectangle.
        """
        return 2 * (self.width + self.height)
    