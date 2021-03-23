if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_12.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import myPackage
import matplotlib.pyplot as plt
import numpy as np


# MNIST 설치
train_set = myPackage.datasets.MNIST(train=True, transform=None)
test_set = myPackage.datasets.MNIST(train=False, transform=None)

print(len(train_set))
print(len(test_set))

# train_set check
x, t = train_set[0]
print(type(x), x.shape)
print(t)

# visualization
plt.imshow(x.reshape(28, 28), cmap='gray')
plt.axis('off')
plt.show()
print('label:', t)

