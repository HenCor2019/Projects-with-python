import numpy as np


array5I = np.array([])
def Function_5i(x,a) :
    tmp = 10
    tmp = 1
    tmp = 2
    while tmp <= x :
        a= np.append(a,5*tmp)
        tmp = tmp + 1
    
    print(a.prod())
    return a.prod()

def Function_5i5i(x,a) :
    tmp = 1
    while tmp <= x :
        a= np.append(a,5*tmp + 5)
        tmp = tmp + 1
    
    print(a)
    print(a.prod())
    return a.prod()

print(Function_5i(100,array5I)/Function_5i5i(100,array5I))

