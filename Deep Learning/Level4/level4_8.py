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

