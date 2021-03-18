if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_9.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
import myPackage.functions as F
import myPackage
from myPackage.dataloaders import DataLoader
from myPackage.models import MLP
from myPackage import optimizers


# # accuracy test
# y = np.array([[0.2, 0.8, 0], [0.1, 0.9, 0], [0.8, 0.1, 0.1]])
# t = np.array([1, 2, 0])
# acc = F.accuracy(y, t)
# print(acc)


max_epoch = 300
batch_size = 30
hidden_size = 10
lr = 1.0

train_set = myPackage.datasets.Spiral(train=True)
test_set = myPackage.datasets.Spiral(train=False)
train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle=False)

model = MLP((hidden_size, 3))
optimizer = optimizers.SGD(lr).setup(model)

for epoch in range(max_epoch):
    sum_loss, sum_acc = 0, 0

    for x, t in train_loader:
        y = model(x)
        loss = F.softmax_cross_entropy(y, t)
        acc = F.accuracy(y, t)
        model.cleargrads()
        loss.backward()
        optimizer.update()

        sum_loss += float(loss.data) * len(t)
        sum_acc += float(acc.data) * len(t)

    print(f'epoch: {epoch + 1}')
    print(f'train loss: {sum_loss / len(train_set)}, accuracy: {sum_acc / len(train_set)}')

    sum_loss, sum_acc = 0, 0
    with myPackage.no_grad():
        for x, t in test_loader:
            y = model(x)
            loss = F.softmax_cross_entropy(y, t)
            acc = F.accuracy(y, t)
            

