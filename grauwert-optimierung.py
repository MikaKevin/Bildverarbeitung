import numpy as np
bw_img = np.genfromtxt("bw_img.csv", delimiter=',')


def IntensityScale(img):
    output = np.zeros((img.shape[0],img.shape[1]))
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            output[x][y] = img[x][y]**2/255
    return output

def InvertImg(img):
    output = np.zeros((img.shape[0],img.shape[1]))
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            output[x][y] = 255-img[x][y]
    return output

def Clipping(img,threshhold):
    output = np.zeros((img.shape[0],img.shape[1]))
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if output[x][y]>= threshhold:
                output[x][y] = img[x][y]
            else:
                output[x][y] = 0
    return output

def nonlineargrayscale(img,weight):
    output = np.zeros((img.shape[0],img.shape[1]))
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            output[x][y] = np.exp(weight*img[x][y])-1
    return output

def gammacorrection(img,gamma):
    output = np.zeros((img.shape[0],img.shape[1]))
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            output[x][y] = 255*(img[x][y]/255)**(1/gamma)
    return output