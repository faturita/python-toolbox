#coding: latin-1

# Akaze are local descriptors that can be used to determine similar patches
# on the image.

# https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html

# import the necessary packages
from __future__ import print_function
import cv2

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour


image = cv2.imread("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo1.pgm")
cv2.imshow("Time 1", image)
cv2.waitKey(0)

oimage = cv2.imread("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo1.pgm")


width, height = image.shape[:2]
print("Image size:" + str((width, height)))

kernel = np.ones((5,5),np.float32)/25
image = cv2.filter2D(image,-1,kernel)


imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cnt = contours[4]
#cv2.drawContours(image, [cnt], 0, (0,255,0), 3)
cv2.drawContours(image, contours, -1, (0,255,0), 3)


cv2.imshow("2", image)
cv2.waitKey(0);

cv2.imwrite("contorno.png",image)



image20 = cv2.imread("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo20.pgm")

cv2.drawContours(image20, contours, -1, (0,255,0), 3)

cv2.imshow("Time 20", image20)
cv2.waitKey(0)

print (contours[0][0])

print (np.shape(contours[0])[0])

for i in range(0,np.shape(contours[0])[0]):
    c = contours[0][i]
    if (c[0][0] == 0):
        print (c[0])
        contours[0] = np.delete(contours[0], i)




c = contours[0]

a = np.where( c == ([0,0]))

print (np.shape(a))


if (False):
    img = oimage
    img = rgb2gray(img)

    s = np.linspace(0, 2*np.pi, 400)
    x = 500 + 470*np.cos(s)
    y = 500 + 470*np.sin(s)
    init = np.array([x, y]).T

    snake = active_contour(gaussian(img, 3),
                           init)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.imshow(img, cmap=plt.cm.gray)
    ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
    ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
    ax.set_xticks([]), ax.set_yticks([])
    ax.axis([0, img.shape[1], img.shape[0], 0])

    plt.show()
