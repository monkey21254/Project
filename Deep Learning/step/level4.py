if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import myPackage.functions as F
from myPackage import Variable

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.sum(x, axis=0)
y.backward()   # gy == variable([1 1 1])
print(y)       # Variable([5 7 9])
print(x.grad)  # Variable([[1 1 1], [1 1 1]])

x = Variable(np.random.randn(2, 3, 4, 5))
y = x.sum(keepdims=True)
print(y.shape) # (1, 1, 1, 1)


