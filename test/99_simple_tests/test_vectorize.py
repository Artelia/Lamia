import numpy as np

def myfunc(a, b):
    "Return a-b if a>b, otherwise return a+b"
    if a > b:
        return a - b
    else:
        return a + b

vfunc = np.vectorize(myfunc)
print(vfunc([1, 2, 3, 4], 2))
print(vfunc([1, 2, 3, 4], [2,3,5,6]))

