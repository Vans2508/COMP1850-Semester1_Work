# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

# Read the file content
from pathlib import Path
image_file = Path(__file__).parent.parent /"images" / "feep.pgm"
try:
    with image_file.open("r") as infile:
        lines = infile.readlines()
    width, height = lines[1].split()
    max_gray_value = lines[2].strip()
    print(f"Dimensions: {width} x {height} pixels")
    print(f"Max Grey Value: {max_gray_value}")
except FileNotFoundError:
    print(f"Error: Could not find {image_file}")


# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)