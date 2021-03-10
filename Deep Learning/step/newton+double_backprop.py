if '__file__' in globals():
    import os, sys
    print('__file__ in globals')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
import myPackage.functions as F
from myPackage import Variable


x = Variable(np.array([1., 2.]))
v = Variable(np.array([4., 5.]))


def f(x):
    t = x ** 2
    y = F.sum(t) ## 업데이트 필요
    return y


y = f(x)
y.backward(create_graph = True)

gx = x.grad
x.cleargrad()

z = F.matmul(v, gx) ## 업데이트 필요
z.backward()
print(x.grad)

