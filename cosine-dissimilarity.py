import time, scipy.spatial.distance, numpy as np
from sklearn.datasets import load_svmlight_file

SSD = getattr(scipy.spatial.distance,'cosine')
fVsm = ''

def Test(vsm, N, func):
    vector = 0.0

    if func == 'SSD':
        waktu = time.time()
        for i in range(N-1):
            vector+=SSD(vsm[i].toarray(),vsm[i+1].toarray())
    else:
        waktu = time.time()
        for i in range(N-1):
            vector+=fCosine(vsm[i], vsm[i+1])
    waktu = time.time()-waktu
    vector = vector/(N-1)
    return waktu, vector

if __name__=="__main__":
    vsm = load_svmlight_file(fVsm)[0]
    N,L = vsm.get_shape()
    print ('Data size = {0} x {1} density = {2}'. format(N,L,vsm.nnz/(N*L)))

    t1,res1 = Test(vsm,N,'SSD')
    t2,res2 = Test(vsm,N,'SSD')
    print('time SSD= {0}, vector {1}'.format(t1,res1))
    print('time fCos={0}, vector {1}'.format(t2,res2))
