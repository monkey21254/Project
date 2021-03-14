if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_7.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import myPackage
import matplotlib.pyplot as plt


x, t = myPackage.datasets.get_spiral(train=True)
print(x.shape)
print(t.shape)

print(x[10], t[10])
print(x[110], t[110])


# Plot data points of the dataset
N, CLS_NUM = 100, 3
markers = ['o', 'x', '^']
colors = ['orange', 'blue', 'green']
for i in range(len(x)):
    c = t[i]
    plt.scatter(x[i][0], x[i][1], s=25,  marker=markers[c], c=colors[c])
plt.show()


