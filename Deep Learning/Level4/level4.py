if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import myPackage.functions as F
from myPackage import Variable, Parameter
import matplotlib.pyplot as plt

# 브로드캐스트, SumTo 연산 확인
x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.sum(x, axis=0)
y.backward()   # gy == variable([1 1 1])
print(y)       # Variable([5 7 9])
print(x.grad)  # Variable([[1 1 1], [1 1 1]])

x = Variable(np.random.randn(2, 3, 4, 5))
y = x.sum(keepdims=True)
print(y.shape) # (1, 1, 1, 1)


# 데이터셋
np.random.seed(0)
x = np.random.rand(100, 1)
y = np.sin(2 * np.pi * x) + np.random.rand(100, 1)

# 가중치 초기화
I, H, O = 1, 10, 1
W1 = Variable(0.01 * np.random.randn(I, H))
b1 = Variable(np.zeros(H))
W2 = Variable(0.01 * np.random.randn(H, O))
b2 = Variable(np.zeros(O))

# 신경망 추론
def predict(x):
    y = F.linear(x, W1, b1)
    y = F.sigmoid(y)
    y = F.linear(y, W2, b2)
    return y

lr = 0.2
iters = 10000

# 신경망 학습
for i in range(iters):
    y_pred = predict(x)
    loss = F.mean_squared_error(y, y_pred)

    W1.cleargrad()
    b1.cleargrad()
    W2.cleargrad()
    b2.cleargrad()
    loss.backward()

    W1.data -= lr * W1.grad.data
    b1.data -= lr * b1.grad.data
    W2.data -= lr * W2.grad.data
    b2.data -= lr * b2.grad.data

    if i % 1000 == 0:
        print(loss)

# matplotlib 결과 확인
plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')
t = np.arange(0, 1, .01)[:, np.newaxis]
y_pred = predict(t)
plt.plot(t, y_pred.data, color='r')
plt.show()


# Parameter Class
x = Variable(np.array(1.))
p = Parameter(np.array(2.))
y = x + p

print(isinstance(p, Variable))
print(isinstance(p, Parameter))
print(isinstance(x, Parameter))
print(isinstance(y, Parameter))


