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
#cv2.waitKey(0)

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
#cv2.waitKey(0);

cv2.imwrite("contorno.png",image)



image20 = cv2.imread("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo20.pgm")

cv2.drawContours(image20, contours, -1, (0,255,0), 3)

cv2.imshow("Time 20", image20)
#cv2.waitKey(0)

print (contours[0][0])

print("Number of curves:")
print (np.shape(contours))

print ("Eliminating the border curve.")
contours = np.delete(contours, 0)

print("Number of curves:")
print (np.shape(contours))

curveindex = []
for i in contours:
    print("Curve length:" + str( np.shape(i)[0]  ) )
    curveindex.append( np.shape(i)[0]  )

ncurveindex = np.array(curveindex)

print("Max length:" + str( ncurveindex.max()   ) + " at " + str(ncurveindex.argmax()))

print ("Reshaping the contour list...")
contours = np.array( contours[ncurveindex.argmax()] )

image20 = cv2.imread("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo20.pgm")
# Otsu's thresholding after Gaussian filtering
imgray = cv2.cvtColor(image20, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(imgray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.drawContours(th3, contours, -1, (0,255,0), 3)

cv2.imshow("Time 20", th3)
cv2.waitKey(0)

# Get the curve
c = contours

for p in c:
    print(p)
    break


print(c.shape)
Xs = c[:, 0,0]
Ys = c[:, 0,1]

print (Xs.shape)
print (Ys.shape)

print (c)
k=0
for x in range(0,np.shape(th3)[0]):
    for y in range(0,np.shape(th3)[1]):
        print ([x,y])
        b = np.where( Xs == x)
        #print (c[b])
        d = np.where( Ys[b] > y)
        #print ("Elements found:" + str(np.shape(d[0])))
        #print (d[0])
        #print (b[0][d[0]])
        #print (c[b[0][d[0]]])

        e = np.where( Ys[b] < y)
        #print ("Elements found:" + str(np.shape(e[0])))
        #print (e[0])
        #print (b[0][e[0]])
        #print (c[b[0][e[0]]])


        if (np.shape(d[0])[0]>0 and np.shape(e[0])[0]>0):
            image20[y,x] = 255
            k = k + 1

cv2.imshow("Time 20", image20)
cv2.waitKey(0)

# Bien funca pero hace lio con las areas inconexas.
# A efectos practicos me sirve.

print (k)
print((k*1.0)/(1024*1024))


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
