from PIL import Image
import sys

im = Image.open("nintendo.png")

im.show()

def scale_to_width(dimensions, width):
    height = (width * dimensions[1]) / dimensions[0]

    return (width, height)

im.resize(scale_to_width(im.size, int(sys.argv[2])), Image.NEAREST).save("scaled.png")


im.show()