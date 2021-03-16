if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_8.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import math
import numpy as np
import myPackage
from myPackage import optimizers
import myPackage.functions as F
from myPackage.models import MLP
import matplotlib.pyplot as plt


# 하이퍼파라미터 설정
max_epoch = 300
batch_size = 30
hidden_size = 10
lr = 1.0

# 데이터셋 및 모델, 옵티마이저 설정
x, t = myPackage.datasets.get_spiral(train=True)
model = MLP((hidden_size, 3))
optimizer = optimizers.SGD(lr).setup(model)

# 학습 진행
data_size = len(x)
max_iter = math.ceil(data_size / batch_size) # 소수점 반올림

epoch_list = []
avg_lost_list = []

for epoch in range(max_epoch):
    # 데이터셋의 인덱스 섞기
    index = np.random.permutation(data_size)
    sum_loss = 0

    for i in range(max_iter):
        # 미니배치 생성
        batch_index = index[i * batch_size : (i + 1) * batch_size]
        batch_x = x[batch_index]
        batch_t = t[batch_index]

        # 기울기 산술 / 매개변수 갱신
        y = model(batch_x)
        loss = F.softmax_cross_entropy(y, batch_t)
        model.cleargrads()
        loss.backward()
        optimizer.update()
        sum_loss += float(loss.data) * len(batch_t)

    # 에포크마다 학습 경과 출력
    avg_loss = sum_loss / data_size
    print("epoch %d, loss %.2f" % (epoch + 1, avg_loss))

    epoch_list.append(epoch + 1)
    avg_lost_list.append(avg_loss)


# Plot loss graph
plt.plot(epoch_list, avg_lost_list)
plt.show()

# Plot boundary area the model predict
h = 0.001
x_min, x_max = x[:, 0].min() - .1, x[:, 0].max() + .1
y_min, y_max = x[:, 1].min() - .1, x[:, 1].max() + .1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
X = np.c_[xx.ravel(), yy.ravel()]
print(xx.ravel(), xx.shape)
print(yy.ravel(), yy.shape)
print(X, X.shape)

with myPackage.no_grad():
    score = model(X)
predict_cls = np.argmax(score.data, axis=1)
print(score.data, score.data.shape)
Z = predict_cls.reshape(xx.shape)
plt.contourf(xx, yy, Z)

# Plot data points of the dataset
N, CLS_NUM = 100, 3
markers = ['o', 'x', '^']
colors = ['orange', 'blue', 'green']
for i in range(len(x)):
    c = t[i]
    plt.scatter(x[i][0], x[i][1], s=40,  marker=markers[c], c=colors[c])
plt.show()

