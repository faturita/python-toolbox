#coding: latin-1
# Tour

# Handy snippets for the hurry programmer.

import cv2
import os
import numpy
import time

image = cv2.imread('01.png')
cv2.imwrite('01.jpg', image)

# image is of type numpy.array

# image[0,0,0], row=y 0, column=x, the third index is the color channel.

print ( image.item ( (0,0,0) ))

np.where( labels == 3 )

print ('Lets convert the numpy array to standard python array:')

bgrByteArray = bytearray( image )

grayImage = numpy.array(bgrByteArray).reshape(image.shape[0], image.shape[1], image.shape[2])

print ('Random image...')

# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)
# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)


videoCapture = cv2.VideoCapture(0)
# Find OpenCV version
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.

if int(major_ver)  < 3 :
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
    print "Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps)
else :
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    print "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Number of frames to capture
num_frames = 120;

print "Capturing {0} frames".format(num_frames)

# Start time
start = time.time()

# Grab a few frames
for i in xrange(0, num_frames) :
    ret, frame = videoCapture.read()


# End time
end = time.time()

# Time elapsed
seconds = end - start
print "Time taken : {0} seconds".format(seconds)

# Calculate frames per second
fps  = num_frames / seconds;
print "Estimated frames per second : {0}".format(fps);

# YUV, 4:2:0
#videoWriter = cv2.VideoWriter('MyVid.avi', cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

#CV_FOURCC('P','I','M','1')    = MPEG-1 codec
#CV_FOURCC('M','J','P','G')    = motion-jpeg codec (does not work well)
#CV_FOURCC('M', 'P', '4', '2') = MPEG-4.2 codec
#CV_FOURCC('D', 'I', 'V', '3') = MPEG-4.3 codec
#CV_FOURCC('D', 'I', 'V', 'X') = MPEG-4 codec
#CV_FOURCC('U', '2', '6', '3') = H263 codec
#CV_FOURCC('I', '2', '6', '3') = H263I codec
#CV_FOURCC('F', 'L', 'V', '1') = FLV1 codec

videoWriter = cv2.VideoWriter('capturevideo.flv', cv2.VideoWriter_fourcc('F', 'L', 'V', '1'), fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
    cv2.imshow("ViewWindow", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoWriter.release()
videoCapture.release()
