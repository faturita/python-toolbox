import numpy as np
import cv2
import sys
import time
import datetime

# Python3 implementation of the approach 
from math import sqrt 

# Function to find the circle on 
# which the given three points lie 
def findCircle(x1, y1, x2, y2, x3, y3): 
    x12 = x1 - x2
    x13 = x1 - x3

    y12 = y1 - y2
    y13 = y1 - y3

    y31 = y3 - y1
    y21 = y2 - y1

    x31 = x3 - x1
    x21 = x2 - x1

    # x1^2 - x3^2 
    sx13 = pow(x1, 2) - pow(x3, 2)

    # y1^2 - y3^2 
    sy13 = pow(y1, 2) - pow(y3, 2)

    sx21 = pow(x2, 2) - pow(x1, 2)
    sy21 = pow(y2, 2) - pow(y1, 2)

    f = (((sx13) * (x12) + (sy13) *
        (x12) + (sx21) * (x13) +
        (sy21) * (x13)) // (2 *
        ((y31) * (x12) - (y21) * (x13))))
            
    g = (((sx13) * (y12) + (sy13) * (y12) +
        (sx21) * (y13) + (sy21) * (y13)) //
        (2 * ((x31) * (y12) - (x21) * (y13))))

    c = (-pow(x1, 2) - pow(y1, 2) -
        2 * g * x1 - 2 * f * y1)

    # eqn of circle be x^2 + y^2 + 2*g*x + 2*f*y + c = 0 
    # where centre is (h = -g, k = -f) and 
    # radius r as r^2 = h^2 + k^2 - c 
    h = -g
    k = -f
    sqr_of_r = h * h + k * k - c

    # r is the radius 
    r = round(sqrt(sqr_of_r), 5)

    print("Centre = (", h, ", ", k, ")")
    print("Radius = ", r)

    return [(h,k),r]

# This code is contributed by Ryuga 


height, width = 200, 200
img = np.zeros((height, width, 3), np.uint8)
img[:, :] = [255, 255, 255]

# Pixel position to draw at
row, col = 100, 100

# # Draw a square with position 20, 100 as the top left corner
# for i in range(row, 30):
#     for j in range(col, 110):
#         img[i, j] = [0, 0, 255]


x1 = 70 ; y1 = 100
x2 = 100 ; y2 = 80
x3 = 120 ; y3 = 100
[(row, col),r] = findCircle(x1, y1, x2, y2, x3, y3)

cv2.circle(img,(int(row), int(col)), int(r), (0,255,0), -1)

cv2.imwrite("square_circle_opencv.jpg", img)

while (True):
    #ret, frame = cap.read()

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S.%f')
    #cv2.rectangle(frame, (420, 205), (595, 385),(0, 0, 255), -1)
    #cv2.putText(img, "T={}".format(st), (10, 30), cv2.FONT_ITALIC , 1.0, (0, 0, 255), 3)

    cv2.imshow('Video Stream', img)

    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord('q'):
        break
