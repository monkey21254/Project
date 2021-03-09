if '__file__' in globals():
    import os, sys
    print('__file__ in globals')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import numpy as np
from myPackage import Variable
from myPackage.utils import plot_dot_graph
import myPackage.functions as F
import matplotlib.pyplot as plt



x = Variable(np.array(1.))
y = F.sin(x)
y.backward(create_graph=True)

for i in range(5):
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)
    print(x.grad)

x.cleargrad()

x = Variable(np.linspace(-7, 7, 200))
y = F.sin(x)
y.backward(create_graph=True)

logs = [y.data]

for i in range(3):
    logs.append(x.grad.data)
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)

labels = ["y=sin(x)", "y'", "y''", "y'''"]
for i, v in enumerate(logs):
    plt.plot(x.data, logs[i], label=labels[i])
plt.legend(loc = 'lower right')
plt.show()

x.cleargrad()
y = F.tanh(x)
x.name = 'x'
y.name = 'y'
y.backward(create_graph=True)

iters = 0

for i in range(iters):
    gx = x.grad
    x.cleargrad()
    gx.backward(create_graph=True)

gx = x.grad
gx.name = 'gx' + str(iters+1)
plot_dot_graph(gx, verbose=False, to_file=f'tanh{iters + 1}.png')