if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_13.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import myPackage
import matplotlib.pyplot as plt
import numpy as np
from myPackage.dataloaders import DataLoader
from myPackage.models import MLP
from myPackage import optimizers
import myPackage.functions as F


# preprocessing func
def f(x):
    x = x.flatten()
    x = x.astype(np.float32)
    x /= 255.0
    return x

train_set = myPackage.datasets.MNIST(train=True, transform=f)
test_set = myPackage.datasets.MNIST(train=False, transform=f)

max_epoch = 5
batch_size = 100
hidden_size = 1000

train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle=False)

# model = MLP((hidden_size, 10)) # F.sigmoid
model = MLP((hidden_size, hidden_size, 10), activation=F.relu)
optimizer = optimizers.SGD().setup(model)

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

    print('epoch: {}'.format(epoch + 1))
    print('train loss: {:.4f}, accuracy: {:.4f}'.format(sum_loss / len(train_set), sum_acc / len(train_set)))

    sum_loss, sum_acc = 0, 0
    with myPackage.no_grad():
        for x, t in test_loader:
            y = model(x)
            loss = F.softmax_cross_entropy(y, t)
            acc = F.accuracy(y, t)
            sum_loss += float(loss.data) * len(t)
            sum_acc += float(acc.data) * len(t)

    print('test loss: {:.4f}, accuracy: {:.4f}'.format(sum_loss / len(test_set), sum_acc / len(test_set)))
        

