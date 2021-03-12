if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_4.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
import myPackage.functions as F
import myPackage.layers as L
from myPackage import Variable, Model


class TwoLayerNet(Model):
    def __init__(self, hidden_size, out_size):
        super().__init__()
        self.l1 = L.Linear(hidden_size)
        self.l2 = L.Linear(out_size)

    def forward(self, x):
        y = F.sigmoid(self.l1(x))
        y = self.l2(y)
        return y


# # TEST1
# x = Variable(np.random.randn(5, 10), name='x')
# model = TwoLayerNet(100, 10)
# model.plot(x)


# # TEST2
np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

lr = 0.2
max_iter = 10000
hidden_size = 10

model = TwoLayerNet(hidden_size, 1)
model.plot(y, to_file="test.png")

# 학습 시작
for i in range(max_iter):
    y_pred = model(x)
    loss = F.mean_squared_error(y, y_pred)

    model.cleargrads()
    loss.backward()

    for p in model.params():
        p.data -= lr * p.grad.data
    if i % 1000 == 0:
        print(loss)
