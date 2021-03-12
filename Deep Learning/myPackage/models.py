if '__file__' in globals():
    import os, sys
    print('__file__ in globals at models.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from myPackage import Layer
from myPackage import utils


class Model(Layer):
    def plot(self, *inputs, to_file='model.png'):
        y = self.forward(*inputs)
        return utils.plot_dot_graph(y, verbose=True, to_file=to_file)


