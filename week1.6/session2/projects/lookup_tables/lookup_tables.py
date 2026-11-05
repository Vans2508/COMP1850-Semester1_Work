import image



lookup = list(range(256))

def apply_lookup(img, lookup):
    img = image.Image()
    img_read = img.read("coins.pgm")
    result = img.copy()

    for i in range(result.width * result.height):
        result[i] = lookup[result[i]]

    return result

img = image.Image()

result = apply_lookup(img, lookup)
print(result.write_pgm("coins_inverted.pgm"))




