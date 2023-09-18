# version: 0.0.1
# author: picklez

import cv2
from numpy import asarray

filename = "testing.png"

im = cv2.imread(filename)
image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

# loading the info as a data array
data = asarray(image)

for col in range(len(data)):
    for row in range(len(data[-1])):
        data[col][row][1] = 0
        data[col][row][0] = 0

cv2.imshow('image edited', data)
cv2.waitKey()
print(data)