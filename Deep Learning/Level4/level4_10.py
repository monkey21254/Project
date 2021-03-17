if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_9.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from myPackage.datasets import Spiral
from myPackage import DataLoader

batch_size = 10
max_epoch = 1

train_set = Spiral(train=True)
test_set = Spiral(train=False)
train_loader = DataLoader(train_set, batch_size)
test_loader = DataLoader(test_set, batch_size, shuffle=False)

for epoch in range(max_epoch):
    for x, t in train_loader:
        print(x.shape, t.shape)
        break

    # 에포크 끝에서 테스트 데이터를 꺼낸다.
    for x, t in test_loader:
        print(x.shape, t.shape)
        break


