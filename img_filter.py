import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread("test.jpg",0)
image_fft = np.fft.fft2(image)


def distance(x1,x2):
    return np.sqrt((x2[0]-x1[0])**2+(x2[1]-x1[1])**2)

def lowpass(threshhold,img):
    output = np.zeros(img.shape)
    rows, cols = img.shape
    center = (rows/2,cols/2)
    for x in range(rows):
        for y in range(cols):
            if distance((x,y),center) < threshhold:
                output[x,y] = 1
    return output
#Highpass would be basically similar
def highpass(threshhold,img):
    output = np.zeros(img.shape)
    rows, cols = img.shape
    center = (rows/2,cols/2)
    for x in range(rows):
        for y in range(cols):
            if distance((x,y),center) > threshhold:
                output[x,y] = 1
    return output
#maybe a smoother filter will be usefull too
def gausfilter(threshhold,img):
    output = np.zeros(img.shape)
    rows, cols = img.shape
    center = (rows/2,cols/2)
    for x in range(rows):
        for y in range(cols):
                output[x,y] = 1 - np.exp(((-distance((x,y),center)**2)/(2*(threshhold**2))))
    return output

#since we're in the frequency domain, we can simply multiply the filter with the 
# fourier transform of the image
lp_filtered_img = image_fft*lowpass(450,image)
#hp_filtered_img = image_fft*highpass(70,image)
gaus_filtered_img = image_fft*gausfilter(10,image)

filtered_img_lp = np.fft.ifft2(lp_filtered_img)
filtered_img_gaus = np.fft.ifft2(gaus_filtered_img)
