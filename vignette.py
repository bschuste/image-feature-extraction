
from PIL import Image
# For help, see the documentation at matplotlib.org
# Also there is a really good youtube video from Corey Schafer
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np

class Vignette:
    def __init__(self, file='data/frame8.ppm'):
        self.file = file

        # Load the captured image
        im = Image.open(self.file)

        # Display its properties
        print("Image size: {}x{}x3 = ".format(im.size[0], im.size[1]), im.size[0]*im.size[1], "pixels")
        print("Image type: ", im.mode, im.format, type(im))
         
        # Convert image into a 3D array of unsigned 8-bit integers
        im.load()
        rgb = np.asarray(im, dtype=np.uint8)

        # Split image into individual color components
        self.R, self.G, self.B = im.split()

        # Display array properties
        print("rgb array shape:", rgb.shape)
        print("rgb array size:", rgb.size)
        print("rgb array data type:", rgb.dtype)
        print("rgb array dimension:", rgb.ndim)

        # Load individual color components in a 2D array
        r = np.asarray(self.R, dtype=np.uint8)
        g = np.asarray(self.G, dtype=np.uint8)
        b = np.asarray(self.B, dtype=np.uint8)

        print("Array Properties:")
        print("  Shape:", rgb.shape)
        print("  Size:", rgb.size)
        print("  Data type:", rgb.size)
        print("  Dimension:", rgb.ndim)
        print("")
        print("                   R   G   B")
        print("Array min values: {:03d} {:03d} {:03d}".format(r.min(), g.min(), b.min()))
        print("Array max values: {:03d} {:03d} {:03d}".format(r.max(), g.max(), b.max()))

        # Keep the image for later use
        self.im = im
        self.rgb = rgb
    
    def get(self):
        return self.rgb

    def show_image(self):
       # This code could be used to display the image but it is not as nice as using plot: self.im.show(title="Original")

        plt.imshow(self.rgb)
        plt.axis('off')
        plt.tight_layout()
        plt.show(block=True)

        # Release memory
        plt.close()
        
        """
        # Alternatively load the image using matplotlib
        ar = mpimg.imread('data/frame8.ppm')
        print(ar.shape, ar.dtype, type(ar))
        plt.figure(figsize=(10,10))
        plt.imshow(ar) # display the image
        plt.axis('off')
        plt.show()
        """

    def show_hist(self):
        # The image histogram is provided as a list of 3x256 values
        # Red: histogram(:256)
        # Green: histogram(256:512)
        # Blue: histogram(512:768)
        print("Displaying two windows")
        histogram = self.im.histogram()
        print("rgb histogram size:", len(histogram))

        # Set the display style
        #print(plt.style.available)
        # default style: fivethirtyeight
        plt.style.use('dark_background')
        # This is a fun style: plt.xkcd()

        # Display Red, Green and Blue histograms on two different windows
        # Draw y values
        plt.figure(1)
        plt.subplot(311)
        plt.plot(histogram[0:256], color='r', linestyle='-', marker='o', label='Red')
        plt.grid(True)
        plt.tight_layout()
        plt.subplot(312)
        plt.plot(histogram[256:512], color='g', linestyle='-', marker='o', label='Green')
        plt.grid(True)
        plt.tight_layout()
        plt.subplot(313)
        plt.plot(histogram[512:768], color='b', linestyle='-', marker='o', label='Blue')
        plt.grid(True)
        plt.tight_layout()
        plt.figure(2)
        plt.plot(histogram[0:256], color='r', linestyle='-', marker='o', label='Red')
        plt.plot(histogram[256:512], color='g', linestyle='-', marker='o', label='Green')
        plt.plot(histogram[512:768], color='b', linestyle='-', marker='o', label='Blue')
        plt.xlabel('0-255')
        plt.ylabel('Occurence per Value')
        plt.title('Histogram of R, G, B components')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('data/histogram.png')
        # This is blocking until the user closes the plot window
        plt.show(block=True)

        # Release memory
        plt.close()
        """
        rh = self.R.histogram()
        print("red histogram size:", len(rh))
        plt.plot(rh, color='r', linestyle='-', marker='o', label='Red')
        plt.show(block=False)
        plt.clf()
        """


if __name__ == "__main__":
    v = Vignette(file='data/frame8.ppm')
    v.show_image()
    v.show_hist()