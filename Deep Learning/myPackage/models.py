if '__file__' in globals():
    import os, sys
    print('__file__ in globals at models.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from myPackage import Layer
from myPackage import utils
import myPackage.functions as F
import myPackage.layers as L


class Model(Layer):
    def plot(self, *inputs, to_file='model.png'):
        y = self.forward(*inputs)
        return utils.plot_dot_graph(y, verbose=True, to_file=to_file)


class MLP(Model): # Multi-Layer Perceptron
    def __init__(self, fc_output_sizes, activation=F.sigmoid):
        super().__init__()
        self.activation = activation
        self.layers = []

        for i, out_size in enumerate(fc_output_sizes):
            layer = L.Linear(out_size)
            setattr(self, 'l' + str(i), layer)
            self.layers.append(layer)

    def forward(self, x):
        for l in self.layers[:-1]:
            x = self.activation(l(x))
        return self.layers[-1](x)
    
