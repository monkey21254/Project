if '__file__' in globals():
    import os, sys
    print('__file__ in globals at layers.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


from myPackage.core_complex import Variable, Parameter
import numpy as np
import weakref
import myPackage.functions as F


class Layer:
    """
    Layer class
    -----------
    input, hidden, output layer에 대한 기반클래스

    Args
    ----
    name: Layer's name.
    value: Layer's value is put in name's attritube.
    inputs: This parameter means layer's input data.

    Method
    ------
    __setattr__: Get parameter(name, value) and check a value's type in Parameter instance. Then, set attribute value about name.
    __call__: Make callable function instance with inputs value(get variable argument)(This method use weakref.ref for help to circular reference.).
    forward: It will be necessary method from derived class.
    params: Yield a layer instances value using iterator.
    cleargrad: Clear all value's gradient.
    >> Update
        to_gpu & to_cpu: Variable 데이터를 GPU or CPU로 전송해주는 기능을 수행하는 메서드
    """
    def __init__(self):
        self._params = set()

    def __setattr__(self, name, value):
        if isinstance(value, (Parameter, Layer)): # Layer 추가
            self._params.add(name)
        super().__setattr__(name, value)

    def __call__(self, *inputs):
        outputs = self.forward(*inputs)
        if not isinstance(outputs, tuple):
            outputs = (outputs,)
        self.inputs = [weakref.ref(x) for x in inputs]
        self.outputs = [weakref.ref(y) for y in outputs]
        return outputs if len(outputs) > 1 else outputs[0]

    def forward(self, inputs):
        raise NotImplementedError()

    def params(self):
        for name in self._params:
            obj = self.__dict__[name]

            if isinstance(obj, Layer): # Layer에서 매개변수 꺼내기
                yield from obj.params()
            else:
                yield obj
        
    def cleargrads(self):
        for param in self.params():
            param.cleargrad()

    def to_cpu(self):
        for param in self.params():
            param.to_cpu()

    def to_gpu(self):
        for param in self.params():
            param.to_gpu()


class Linear(Layer):
    """
    Linear Class
    
    Args
    ----
    in_size, out_size: input array's size, output array's size
    nobias: Flag select to use bias or not.

    Method
    ------
    __init__: Set argument from the paramter. Then according to nobias config, self.b is decided from config.
    _init_W: Initialize the weight ndarray and set dtype.
    forward: Work linear forward propagation.
    """
    def __init__(self, out_size, nobias=False, dtype=np.float32, in_size=None):
        super().__init__()
        self.in_size = in_size
        self.out_size = out_size
        self.dtype = dtype

        self.W = Parameter(None, name='W')
        if self.in_size is not None: # in_size가 정의되지 않은 경우 나중으로 연기
            self._init_W()

        if nobias:
            self.b = None
        else:
            self.b = Parameter(np.zeros(out_size, dtype=dtype), name='b')


    def _init_W(self):
        I, O = self.in_size, self.out_size
        W_data = np.random.randn(I, O).astype(self.dtype) * np.sqrt(1 / I)
        self.W.data = W_data


    def forward(self, x):
        # 데이터를 흘려보내는 시점에 가중치를 초기화
        if self.W.data is None:
            self.in_size = x.shape[1]
            self._init_W()

        y = F.linear(x, self.W, self.b)
        return y


if __name__ == '__main__':
    # TEST
    layer = Layer()

    layer.p1 = Parameter(np.array(1))
    layer.p2 = Parameter(np.array(2))
    layer.p3 = Variable(np.array(3))
    layer.p4 = 'test'

    print(layer._params)
    print('------------')

    for name in layer._params:
        print(name, layer.__dict__[name], layer.__dict__)


