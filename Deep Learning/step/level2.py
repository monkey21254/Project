if '__file__' in globals():
    import os, sys
    print('__file__ in globals') # __file__ : d:\python\step\level2.py
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from Level2 import Variable

x = Variable(np.array(1.))
y = (x + 3) ** 2
y.backward()

print(y)
print(x.grad)