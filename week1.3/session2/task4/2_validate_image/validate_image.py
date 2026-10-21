# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

# Select the image you want to test.
image_file = "../images/gradient.pgm"

try:
    with open(image_file, "r", encoding="utf-8") as infile:
        lines = []

        for line in infile:
            line = line.strip()

            # Ignore empty lines and comments.
            if line and not line.startswith("#"):
                lines.append(line)

    # PGM file structure:
    # Line 1: file type, for example P2
    # Line 2: width and height
    # Line 3: maximum gray value
    # Remaining lines: pixel values

    width, height = map(int, lines[1].split())
    maximum_gray_value = int(lines[2])

    pixel_rows = []

    for line in lines[3:]:
        row = list(map(int, line.split()))
        pixel_rows.append(row)

    # Check the number of pixels in each row.
    invalid_width = any(len(row) != width for row in pixel_rows)

    # Check the number of rows.
    invalid_height = len(pixel_rows) != height

    # Flatten all rows into one list of pixel values.
    pixels = [pixel for row in pixel_rows for pixel in row]

    invalid_pixels = any(
        pixel < 0 or pixel > maximum_gray_value
        for pixel in pixels
    )

    if invalid_width:
        print("Invalid width")
    elif invalid_height:
        print("Invalid height")
    elif invalid_pixels:
        print("Invalid pixel values")
    else:
        print("Valid image")

except FileNotFoundError:
    print(f"Error: Could not find '{image_file}'.")

except ValueError:
    print("Error: The image contains invalid numerical data.")