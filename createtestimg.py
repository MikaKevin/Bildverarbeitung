import numpy as np
import random
import matplotlib.pyplot as plt
def createTestImg(height,wide, rectheight, rectwide):
    output = np.zeros((height,wide))
    init_x = random.randint(rectwide,wide-rectwide)
    init_y = random.randint(rectheight,wide-rectwide)
    for x in range(init_x,init_x+rectwide):
        for y in range(init_y,init_y+rectheight):
            output[x][y] = 255
    return output
            
#testimg1 = createTestImg(256,256,20,20)
#plt.imshow(testimg1)
#testimg2 = createTestImg(256,256,20,20)
#plt.imshow(testimg2)

np.savetxt("testimg2.csv", testimg2, delimiter=",")