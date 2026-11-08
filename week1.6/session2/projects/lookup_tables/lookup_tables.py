import image
from pathlib import Path

input_file = Path(__file__).resolve().parents[2] / "images" / "coins.pgm"
img = image.Image.read(input_file)
lookup = [255 - value for value in range(256)]
result = img.copy()

for i in range(result.width * result.height):
    result[i] = lookup[result[i]]

result.write_pgm(Path(__file__).with_name("coins_inverted.pgm"))



