import numpy as np
import matplotlib.pyplot as plt

from vignette import Vignette


def convert2ycbcr(rgb):
    # (r, g, b)  .  YCBCR Matrix
    #                 Y         Cb        Cr
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                  [ 0.58700, -0.33126, -0.41869],
                  [ 0.11400,  0.50000, -0.08131]])
    ycbcr = np.dot(rgb, m)
    # convert Cb and Cr from signed to unsigned
    ycbcr[:,:,1:]+=128.0
    # convert to 8-bit
    ycbcr = ycbcr.clip(0, 255).astype('uint8')
    print("ycbcr shape:", ycbcr.shape)
    return ycbcr

def process():
    file = 'data/frame80.ppm'
    v = Vignette(file=file)

    # Retrieve the 3d array of samples as numpy ndarray
    rgb = v.get()

    # Convert into to YCbCr
    ycbcr = convert2ycbcr(rgb)
    print("type(ycbcr)", type(ycbcr))

    # Compute luminance average
    y_average = ycbcr[:,:,0].mean()
    print("y_average", y_average)
    print("y_max", ycbcr[:,:,0].max())
    print("y_min", ycbcr[:,:,0].min())

    # Compute median
    y_median = np.median(ycbcr[:,:,0])
    print("y_median", y_median)

    v.show_image(ycbcr)
    v.show_hist()


if __name__ == "__main__":
    process()
