if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level5_1.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import cupy as cp
import numpy as np


x = cp.arange(6).reshape(2, 3)
y = np.array([1, 2, 3])

# NumPy to CuPy
a = cp.asarray(y)
print(a)
print(type(a))
print(type(y))
assert type(a) == cp.ndarray

# CuPy to NumPy
b = cp.asnumpy(x)
print(b)
print(type(b))
print(type(x))
assert type(b) == np.ndarray


xp = cp.get_array_module(y)
assert xp == np
xp = cp.get_array_module(x)
assert xp == cp

