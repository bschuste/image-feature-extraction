
from PIL import Image
import numpy as np
# For help, see the documentation at matplotlib.org
# Also there is a really good youtube video from Corey Schafer
from matplotlib import pyplot as plt

# Load the captured image
im = Image.open('data/frame8.ppm')

# Display it and its properties
im.show(title="Original")
print("Image size: {}x{}x3 = ".format(im.size[0], im.size[1]), im.size[0]*im.size[1], "pixels")

# The image histogram is provided as a list of 3x256 values
# Red: histogram(:256)
# Green: histogram(256:512)
# Blue: histogram(512:768)
histogram = im.histogram()
print("rgb histogram size:", len(histogram))

# Set the display style
#print(plt.style.available)
# fivethirtyeight
plt.style.use('dark_background')
# This is a fun style: plt.xkcd()

# Display Red, Green and Blue histograms
plt.xlabel('0-255')
plt.ylabel('Occurence per Value')
plt.title('Histogram of R, G, B components')

# Draw y values
plt.plot(histogram[0:256], color='r', linestyle='-', marker='o', label='Red')
plt.plot(histogram[256:512], color='g', linestyle='-', marker='o', label='Green')
plt.plot(histogram[512:768], color='b', linestyle='-', marker='o', label='Blue')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('histogram.png')
plt.show()
plt.clf()

R, G, B = im.split()
rh = R.histogram()
print("red histogram size:", len(rh))
plt.plot(rh, color='r', linestyle='-', marker='o', label='Red')
plt.show()

# Load data into a 3D array of unsigned 8-bit integers
im.load()
rgb = np.asarray(im, dtype=np.uint8)

# Display array properties
print("rgb array shape:", rgb.shape)
print("rgb array size:", rgb.size)
print("rgb array data type:", rgb.dtype)
print("rgb array dimension:", rgb.ndim)

# Load individual color components in a 2D array
r = np.asarray(R, dtype=np.uint8)
print("r array shape:", r.shape)
print("r array size:", r.size)
print("r array data type:", r.dtype)
print("r array dimension:", r.ndim)
