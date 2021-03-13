#easiest thing to do: add black/white pictures

import numpy as np
bw_img = np.genfromtxt("bw_img.csv", delimiter=',')

def addimgs(img1,img2):
    output = np.zeros((img1.shape1[0],img1.shape1[1]))
    for x in range(img1.shape[0]):
        for y in range(img1.shape[1]):
            output[x][y] = img1[x][y]+img2[x][y]
    return output

def diffimg(img1,img2):
    output = np.zeros((img1.shape1[0],img1.shape1[1]))
    for x in range(img1.shape[0]):
        for y in range(img1.shape[1]):
            output[x][y] = img1[x][y]-img2[x][y]
    return output

def mean(img1,img2,img3):
    output = np.zeros((img1.shape1[0],img1.shape1[1]))
    for x in range(img1.shape[0]):
        for y in range(img1.shape[1]):
            output[x][y] = np.mean((img1[x][y],img2[x][y],img3[x][y]))
    return output
