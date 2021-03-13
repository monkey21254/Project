if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_6.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from myPackage import Variable, as_variable
import myPackage.functions as F
from myPackage.models import MLP


# step46
x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.get_item(x, 1)
print(y)

y.backward()
print(x.grad)

# step47
model = MLP((10, 3))

# 소프트맥스(activation func)
x = np.array([[0.2, -0.4], [0.3, 0.5], [1.3, -3.2], [2.1, 0.3]])
y = model(x)
print(y)


def softmax1d(x):
    x = as_variable(x)
    y = F.exp(x)
    sum_y = F.sum(y)
    return y / sum_y


x = Variable(np.array([[0.2, -0.4]]))
y = model(x)
p = softmax1d(y)
print(y)
print(p)


# 교차 엔트로피 오차(loss func)
x = np.array([[0.2, -0.4], [0.3, 0.5], [1.3, -3.2], [2.1, 0.3]])
t = np.array([2, 0, 1, 0])
y = model(x)
loss = F.softmax_cross_entropy_simple(y, t)
""" np.range(N): [0, 1, 2, 3], t.data: [2, 0, 1, 0] >> (0, 2), (1, 0), (2, 1), (3, 0)에 각각 대응
--- log_p ---
variable([[-0.7297049  -1.50558942 -1.21718536]
          [-0.78483925 -1.34828252 -1.25835476]
          [-0.58378107 -1.72674928 -1.33046994]
          [-0.88178794 -1.26541056 -1.19127185]])
--- tlog_p ---
variable([-1.21718536 -0.78483925 -1.72674928 -0.88178794])
"""
print(loss)

