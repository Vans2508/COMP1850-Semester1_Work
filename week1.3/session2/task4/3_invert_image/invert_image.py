# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"

# The input file is in the images folder.
# This relative path works when running the script from this folder:
# week1.3/session2/task4/3_invert_image
input_file = "../images/feep.pgm"

# This is the file that will contain the inverted image.
# It will be created inside the current folder.
output_file = "inverted.pgm"


try:
    # Open the original PGM image for reading.
    #
    # "r" means read mode.
    # encoding="utf-8" tells Python how to interpret the text characters.
    with open(input_file, "r", encoding="utf-8") as infile:

        # Read every line from the image into a list.
        lines = infile.readlines()

    # Remove empty lines and comment lines.
    #
    # PGM comments begin with "#".
    # Keeping only non-empty, non-comment lines makes the file
    # easier to process.
    lines = [
        line.strip()
        for line in lines
        if line.strip() and not line.strip().startswith("#")
    ]

    # The first line identifies the file as a text-based PGM image.
    file_type = lines[0]

    # The second line contains the image width and height.
    # For example: "24 7"
    width, height = map(int, lines[1].split())

    # The third line contains the maximum possible gray value.
    # For example: "15"
    maximum_gray = int(lines[2])

    # The remaining lines contain the pixel values.
    pixel_lines = lines[3:]

    # This list will store the inverted rows of pixels.
    inverted_pixel_lines = []

    # Process one row of pixels at a time.
    for line in pixel_lines:

        # Convert the pixel values from strings to integers.
        #
        # Example:
        # "0 3 7 15" becomes [0, 3, 7, 15]
        pixels = [int(value) for value in line.split()]

        # Invert every pixel.
        #
        # The formula is:
        # inverted pixel = maximum gray value - original pixel
        #
        # If maximum_gray is 15:
        # 0 becomes 15
        # 3 becomes 12
        # 15 becomes 0
        inverted_pixels = [
            maximum_gray - pixel
            for pixel in pixels
        ]

        # Convert the inverted integer values back to strings
        # and join them with spaces.
        #
        # Example:
        # [15, 12, 8, 0] becomes "15 12 8 0"
        inverted_line = " ".join(
            str(pixel)
            for pixel in inverted_pixels
        )

        # Store the completed row.
        inverted_pixel_lines.append(inverted_line)

    # Open the output file for writing.
    #
    # "w" means write mode.
    # If inverted.pgm already exists, its contents are replaced.
    with open(output_file, "w", encoding="utf-8") as outfile:

        # Write the PGM file type.
        outfile.write(f"{file_type}\n")

        # Write the image width and height.
        outfile.write(f"{width} {height}\n")

        # Write the maximum gray value.
        outfile.write(f"{maximum_gray}\n")

        # Write every inverted row of pixels.
        for line in inverted_pixel_lines:
            outfile.write(f"{line}\n")

    # Confirm that the output file was created.
    print(f"Inverted image written to {output_file}")


# This error occurs if the input image cannot be found.
except FileNotFoundError:
    print(f"Error: Could not find {input_file}")


# This error occurs if part of the file cannot be converted to a number.
except ValueError:
    print("Error: The image contains invalid numerical data.")