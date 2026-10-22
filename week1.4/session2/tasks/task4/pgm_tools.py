
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''
    # open a file for reading
    with open(filename,"r") as f:
        # read the PGM header
        header = f.readline().strip()  # read the first line and strip whitespace
        if header != "P2":
            raise ValueError("Not a valid PGM file")  # check if the header is valid

        # read the width and height
        width, height = map(int, f.readline().strip().split())  # read the second line and split into width and height

        # read the max gray value
        max_gray = int(f.readline().strip())  # read the third line for max gray value

        # read the pixel data
        pixels = []
        for _ in range(height):  # iterate over each row of pixels
            row = list(map(int, f.readline().strip().split()))  # read a row of pixel values and convert to integers
            pixels.append(row)  # append the row to the pixel array
        return width, height, max_gray, pixels  # return the image data as a tuple

def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # open a file for writing
    with open(filename,"w") as f:
        # write the PGM header
        f.write("P2\n")  # write the PGM number
        f.write(f"{width} {height}\n")  # write the width and height
        f.write(f"{max_gray}\n")  # write the max gray value

        # write the pixel data
        for row in pixels:  # iterate over each row of pixels
            f.write(" ".join(map(str, row)) + "\n")  # convert pixel values to strings and join with spaces, then write to file using map as a function to convert each pixel value to a string and join them with spaces, then write the row to the file followed by a newline character.

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple
    inverted_pixels = []  # create an empty list to store the inverted pixel values
    for row in pixels:  # iterate over each row of pixels
        inverted_row = [max_gray - pixel for pixel in row]  # invert each pixel value using a list comprehension to subtract each pixel value from the max gray value and create a new list of inverted pixel values for the row
        inverted_pixels.append(inverted_row)  # append the inverted row to the inverted pixel array
    return width,height,max_gray,inverted_pixels  # return the inverted image data as a tuple

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"Original image: {image[3]}")

# write further code to test your own functions

inverted_image = invertPGM(image)
print(writePGM("images/feep_inverted.pgm", inverted_image))

print(f"Image with width {inverted_image[0]} and height {inverted_image[1]}")
print(f"Inverted image: {inverted_image[3]}")