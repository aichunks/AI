import numpy as np
import math
#class Wrap
class Wrap :
    def __init__(self):
        print("")

    # cylindricalwrapping of a image
    def cylindricalWarpImage(self,img1, K, savefig=False) :
        f = K[0, 0]

        im_h, im_w,_ = img1.shape

        # go inverse from cylindrical coord to the image
        # (this way there are no gaps)
        cyl = np.zeros_like(img1)
        cyl_mask = np.zeros_like(img1)
        cyl_h, cyl_w,_= cyl.shape
        x_c = float(cyl_w) / 2.0
        y_c = float(cyl_h) / 2.0
        for x_cyl in np.arange(0, cyl_w):
            for y_cyl in np.arange(0, cyl_h):
                theta = (x_cyl - x_c) / f
                h = (y_cyl - y_c) / f

                X = np.array([math.sin(theta), h, math.cos(theta)])
                X = np.dot(K, X)
                x_im = X[0] / X[2]
                if x_im < 0 or x_im >= im_w:
                    continue

                y_im = X[1] / X[2]
                if y_im < 0 or y_im >= im_h:
                    continue

                cyl[int(y_cyl), int(x_cyl)] = img1[int(y_im), int(x_im)]
                cyl_mask[int(y_cyl), int(x_cyl)] = 255
        return (cyl, cyl_mask)
