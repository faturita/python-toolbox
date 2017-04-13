#coding: latin-1

# Use me to load comma separated dataset files.


import numpy as np
m = np.loadtxt('/Users/rramele/Desktop/Data/Rodrigo/eeg_EyesOpen_1.dat', delimiter=' ', usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14))
m[1:2]
print m[1:2]
