if '__file__' in globals():
    import os, sys
    print('__file__ in globals') # __file__ : d:\python\step\level2.py
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from myPackage import Variable

# TEST
x = Variable(np.array(1.))
y = (x + 3) ** 2
y.backward()

print(f'y: {y}') # variable(16.0) from class's __repr__
print(f'x.grad: {x.grad}') # 8.0

# Sphere Function
def sphere(x, y):
    z = x ** 2 + y ** 2
    return z

x = Variable(np.array(1.))
y = Variable(np.array(1.))
z = sphere(x, y)
z.backward()
print(f'x.grad, y.grad: {x.grad}, {y.grad}') # 2.0, 2.0

# Matyas Function
def matyas(x, y):
    z = 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y
    return z

x = Variable(np.array(1.))
y = Variable(np.array(1.))
z = matyas(x, y)
z.backward()
print(f'x.grad, y.grad: {x.grad}, {y.grad}') # 0.0400000000, 0.040000000000

# Goldstein-Price Function
def goldstein(x, y):
    z = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * \
        (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return z

x = Variable(np.array(1.))
y = Variable(np.array(1.))
z = goldstein(x, y)
z.backward()
print(f'x.grad, y.grad: {x.grad}, {y.grad}') # -5376.0, 8064.0
