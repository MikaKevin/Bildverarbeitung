import numpy as np
from PIL import Image
image = Image.open('testimg.png')
raw_img = np.array(image)
def RGBtoBW(img):
    rows = img.shape[0]
    cols = img.shape[1]
    img_bw = np.zeros((rows,cols))
    for x in range(rows):
        for y in range(cols):
            for z in range(3):#maybe the weights need to be adjusted...
                img_bw[x][y]= 0.3*img[x][y][0]+0.59*img[x][y][1]+0.11*img[x][y][2]
    return img_bw

bw_img = RGBtoBW(raw_img)
np.savetxt("bw_img.csv", bw_img, delimiter=",")