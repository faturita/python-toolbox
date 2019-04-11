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

def processsequence(image1filename, image20filename):

    image = cv2.imread(image1filename)
    cv2.imshow("Neurosphere Time 1", image)
    cv2.waitKey(0)

    oimage = cv2.imread(image20filename)

    width, height = image.shape[:2]
    print("Image size:" + str((width, height)))

    print("Filtered Image.")
    kernel = np.ones((5,5),np.float32)/25
    image = cv2.filter2D(image,-1,kernel)
    cv2.imshow("Neurosphere Time 1 - Filtered", image)
    cv2.waitKey(0)

    print("Active contours")
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #cnt = contours[4]
    #cv2.drawContours(image, [cnt], 0, (0,255,0), 3)
    cv2.drawContours(image, contours, -1, (0,255,0), 3)


    cv2.imshow("Neurosphere Time 1 - Filtered with contours", image)
    cv2.waitKey(0);
    cv2.imwrite("contorno.png",image)

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

    print("Neurosphere Final Time")
    image20 = oimage
    cv2.drawContours(image20, contours, -1, (0,255,0), 3)

    cv2.imshow("Neurosphere Final Time", image20)
    cv2.waitKey(0)

    # Get the longer curve
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
    innerpixels = 0
    for x in range(0,np.shape(image20)[0]):
        for y in range(0,np.shape(image20)[1]):
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
                #image20[y,x] = 255
                innerpixels = innerpixels + 1
            else:
                image20[y,x] = 0

    print("OTSU thresholding")
    # Otsu's thresholding after Gaussian filtering
    imgray = cv2.cvtColor(image20, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    cv2.drawContours(th3, contours, -1, (0,255,0), 3)

    cv2.imshow("Neurosphere Final Time - OTSU Thresholding", th3)
    cv2.waitKey(0)

    topotecanpixels=0
    for x in range(0,np.shape(th3)[0]):
        for y in range(0,np.shape(th3)[1]):
            print ([x,y])
            if (th3[y,x] > 250):
                topotecanpixels = topotecanpixels + 1

    # Bien funca pero hace lio con las areas inconexas.
    # A efectos practicos me sirve.

    print (topotecanpixels)
    result = (topotecanpixels*1.0)/(innerpixels*1.0)
    return result

values = []
#val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N1/PGM/Tiempo20.pgm")
#print("Individuo 2:GRANDES:N1"+ str(val))
#values.append(val)
#val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N2/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N2/PGM/Tiempo14.pgm")
#print("Individuo 2:GRANDES:N2:"+ str(val))
#values.append(val)
#val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N3/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/GRANDES/N3/PGM/Tiempo4.pgm")
#print("Individuo 2:GRANDES:N3:"+ str(val))
#values.append(val)
# PROBLEM;A val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/MEDIANAS/N1/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/MEDIANAS/N1/PGM/Tiempo6.pgm")
#print("Individuo 2:MEDIANAS:N1:"+ str(val))
#values.append(val)
# PROBLEA val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/MEDIANAS/N2/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/MEDIANAS/N2/PGM/Tiempo11.pgm")
#print("Individuo 2:MEDIANAS:N2:"+ str(val))
#values.append(val)
# PROBLEMA val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/PEQUEÑAS/N1/PGM/Tiempo1.pgm","../fotosverdes/FotosOriginales/Individuo 2/PEQUEÑAS/N1/PGM/Tiempo6.pgm")
#print("Individuo 2:PEQUEÑAS:N1:"+ str(val))
#values.append(val)
val = processsequence("../fotosverdes/FotosOriginales/Individuo 2/PEQUEÑAS/N2/PGM/Suavizadas/TiempoN2Suavizada1.pgm","../fotosverdes/FotosOriginales/Individuo 2/PEQUEÑAS/N2/PGM/Suavizadas/TiempoN2Suavizada11.pgm")
print("Individuo 2:PEQUEÑAS:N2:"+ str(val))
values.append(val)
