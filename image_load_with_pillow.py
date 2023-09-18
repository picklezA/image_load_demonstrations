# version: 0.0.1
# author: picklez

# import pillow (aka PIL)
from PIL import Image
# importing numpy so we can view the image as an array
from numpy import asarray

filename = "testing.png"

# pillow can be either PNG or JPEG
# lets load an image and display basic info
image = Image.open(filename)
print(image.format)
print(image.size)
print(image.mode)
#image.show()

# loading the info as a data array
data = asarray(image)
print(type(data))
print(data.shape)

# how to reference the data array:
# data by default is a 3D object = [height][width][RGB Value]
print(len(data[-1][-1]))