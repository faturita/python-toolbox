# coding: latin-1


import scipy.io
mat = scipy.io.loadmat('/Users/rramele/GoogleDrive/BCI.Dataset/008-2014/A01.mat')

mat['data'][0][0][0]


# Labels
mat['data'][0][0][0][0][0]

# Data points
mat['data'][0][0][1]

# Targets / No tagets
mat['data'][0][0][2]

# Data point zero for the eight channels.
mat['data'][0][0][1][0]


import matplotlib.pyplot as plt

data=mat['data'][0][0][1]
cz = data[:,1]

plt.plot(cz)
plt.ylabel('First Channel')
plt.show()
