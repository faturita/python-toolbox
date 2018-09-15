def func(x):
   return ( (-1)*x*x*x+4*x*x-7*x+9 )
   
def one(x):
   return (-1)*x*x*x
   
def two(x):
   return 4*x*x
   
def three(x):
   return -7*x
   
def four(x):
   return 9
   
def all(x):
    print str(one(x)) + ' ' + str(two(x)) + ' ' + str(three(x)) + ' ' + str(four(x))
    print func(x)
    
all(2.75)