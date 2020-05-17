'''
Python Multiprogramming example.

Using pool with 4 processors in a map reduce style.
The performance improvement should be noticed 

Reference: https://towardsdatascience.com/a-hands-on-guide-to-multiprocessing-in-python-48b59bfcc89e
'''

import time
import multiprocessing
import os


def is_prime(n):
      if (n <= 1) : 
          return False
      if (n <= 3) : 
          return True
          
      if (n % 2 == 0 or n % 3 == 0) : 
          return False
    
      i = 5
      while(i * i <= n) : 
          if (n % i == 0 or n % (i + 2) == 0) : 
              return False
          i = i + 6
    
      return True
      
def form(x): 
    if (x): 
        return 'prime' 
    else: 
        return 'not prime'


def multiprocessing_func(x):
    #time.sleep(2)
    v = is_prime(x)
    
    #print('{} is {} number'.format(x, form(v)))

    return v
    
if __name__ == '__main__':
    print('Number of processors {}.'.format(multiprocessing.cpu_count()))
    starttime = time.time()
    results=[]
    for i in range(1,10000000):
        results.append(multiprocessing_func(i))
    print()
    print('Single Process: Time taken = {} seconds'.format(time.time() - starttime))    
    starttime = time.time()
    pool = multiprocessing.Pool(processes=4)
    results = pool.map(multiprocessing_func, range(1,10000000))
    pool.close()
    print()
    print('Parallel:Time taken = {} seconds'.format(time.time() - starttime))

    #print(results)