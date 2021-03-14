import numpy as np
from myPackage.core_complex import Function
from myPackage.core_complex import as_variable
from myPackage import utils
from myPackage import cuda


# ==============================================
# Basic functions: sin / cos / tanh / exp / log
# ==============================================
class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * cos(x)
        return gx

def sin(x):
    return Sin()(x)


class Cos(Function):
    def forward(self, x):
        y = np.cos(x)
        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy * -sin(x)
        return gx
    
def cos(x):
    return Cos()(x)


class Tanh(Function):
    def forward(self, x):
        y = np.tanh(x)
        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = gy * (1 - y * y)
        return gx

def tanh(x):
    return Tanh()(x)


class Exp(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.exp(x)
        return y

    def backward(self, gy):
        y = self.outputs[0]() # weakref
        gx = gy * y
        return gx

def exp(x):
    return Exp()(x)


class Log(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.log(x)
        return y

    def backward(self, gy):
        x, = self.inputs
        gx = gy / x
        return gx

def log(x):
    return Log()(x)


# =============================================================================
# Tensor operations: reshape / transpose / get_item / expand_dims / flatten
# =============================================================================
class Reshape(Function):
    """
    Reshape Class

    Methods
    -------
    __init__ : Get parameter(shape) means ndarray.shape and save that.
    forward : Work forward propagation with parameter(x) is data from variable class's instance. This methods's goal is save the x's shape and change the shape by self.shape.
    backward : Work backward propagation with parameter(gy) is Variable class's instance (come from previous layer having Function.outputs.grad). In this work, this function works reshape variable's shape for match to forward ndarray's shape.
    """
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        y = x.reshape(self.shape)
        return y

    def backward(self, gy):
        return reshape(gy, self.x_shape)

def reshape(x, shape):
    """
    Def reshape

    Explanation
    -----------
    Get parameter(shape) is ndarray.shape and reshape parameter(x)'s shape from parameter(shape).
    """
    if x.shape == shape:
        return as_variable(x)
    return Reshape(shape)(x)


class Transpose(Function):
    """
    Transpose Class

    Methods
    -------
    __init__ : Get parameter(axes) means ndarray's axes by used transpose function(numpy).
    forward : Work forward propagation with parameter(x) is data from variable class's instance. This methods's goal is using function that is numpy module's.
    backward : Work backward propagation with parameter(gy) is Variable class's instance (come from previous layer having Function.outputs.grad). In this work, if self.axes is not None, gy instance have changed by np.argsort for match the forward variable's shape.
    """
    def __init__(self, axes=None):
        self.axes = axes

    def forward(self, x):
        y = x.transpose(self.axes)
        return y

    def backward(self, gy):
        if self.axes is None:
            return transpose(gy)
        
        axes_len = len(self.axes)
        inv_axes = tuple(np.argsort([ax % axes_len for ax in self.axes]))
        return transpose(gy, inv_axes)

def transpose(x, axes=None):
    return Transpose(axes)(x)


class GetItem(Function):
    def __init__(self, slices):
        self.slices = slices

    def forward(self, x):
        y = x[self.slices]
        return y

    def backward(self, gy):
        x, = self.inputs
        f = GetItemGrad(self.slices, x.shape)
        return f(gy)


def get_item(x, slices):
    return GetItem(slices)(x)


class GetItemGrad(Function):
    def __init__(self, slices, in_shape):
        self.slices = slices
        self.in_shape = in_shape
    
    def forward(self, gy):
        gx = np.zeros(self.in_shape)
        np.add.at(gx, self.slices, gy)
        return gx

    def backward(self, ggx):
        return get_item(ggx, self.slices)


# =============================================================================
# sum / sum_to / broadcast_to / average / matmul / linear
# =============================================================================
class Sum(Function):
    """
    Sum Class

    Args
    ----
    gy : It means an input parameter to get result(gx(using functions.broadcast_to)) from previous backprop gradient.

    Methods
    -------
    __init__ : Get parameters(axis, keepdims) for saving configs. An options(Axis and keepdims) are used at np.sum function and backpropagation.
    forward : Using x(Variable.data), y is resulted from x.sum(numpy.sum) and options(axis, keepdims).
    backward : This function need to return gx(Variable.data) using utils.reshape_sum_backward to get sum variable's original form(shape). So gy is used to function(boradcast_to) and get origin form(x_shape) and gx(Variable.data).
    """
    def __init__(self, axis, keepdims):
        self.axis = axis
        self.keepdims = keepdims

    def forward(self, x):
        self.x_shape = x.shape
        y = x.sum(axis=self.axis, keepdims=self.keepdims)
        return y

    def backward(self, gy):
        gy = utils.reshape_sum_backward(gy, self.x_shape, self.axis, self.keepdims)
        gx = broadcast_to(gy, self.x_shape)
        return gx

def sum(x, axis=None, keepdims=False):
    return Sum(axis, keepdims)(x)


class BroadcastTo(Function):
    """
    BroadcastTo Class

    Methods
    -------
    __init__ : Get parameters(shape) for saving configs. An option is used at np.broadcast_to function and backpropagation.
    forward : Calculate an array to apply broadcast with ndarray.shape.
    backward : Broadcast and SumTo classes are an exclusive relationship between forward prop and backward prop.
    """
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        y = np.broadcast_to(x, self.shape)
        return y

    def backward(self, gy):
        gx = sum_to(gy, self.x_shape)
        return gx

def broadcast_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return BroadcastTo(shape)(x)


class SumTo(Function):
    """
    SumTo Class

    Methods
    -------
    __init__ : Get parameters(shape) for saving configs. An option is used at utils.sum_to function to get suqeezed ndarray.shape(Variable.data) and backpropagation.
    forward : Calculate an array to apply sum_to function with ndarray.shape.
    backward : Broadcast and SumTo classes are an exclusive relationship between forward prop and backward prop.
    """
    def __init__(self, shape):
        self.shape = shape

    def forward(self, x):
        self.x_shape = x.shape
        y = utils.sum_to(x, self.shape)
        return y

    def backward(self, gy):
        gx = broadcast_to(gy, self.x_shape)
        return gx

def sum_to(x, shape):
    if x.shape == shape:
        return as_variable(x)
    return SumTo(shape)(x)


class MatMul(Function):
    """
    MatMul Class

    Methods
    -------
    forward : Calculate an multipled array using np.dot(a, b).
    backward : The parameters(gx and gW) are get from matmul function. And this parameters are applied to back-propagation(In short, b.p.) after this layer(s).
    """
    def forward(self, x, W):
        y = x.dot(W)
        return y

    def backward(self, gy):
        x, W = self.inputs
        gx = matmul(gy, W.T)
        gW = matmul(x.T, gy)
        return gx, gW

def matmul(x, W):
    return MatMul()(x, W)


class Linear(Function):
    """
    Linear Class

    Methods
    -------
    forward : Calculate a y means x*W(dot product).
    backward : Perform back-prop from forward-prop equation (x*W + b = y).
    """    
    def forward(self, x, W, b):
        y = x.dot(W)
        if b is not None:
            y += b
        return y

    def backward(self, gy):
        x, W, b = self.inputs
        gb = None if b.data is None else sum_to(gy, b.shape)
        gx = matmul(gy, W.T)
        gW = matmul(x.T, gy)
        return gx, gW, gb


def linear(x, W, b=None):
    return Linear()(x, W, b)


def linear_simple(x, W, b=None):
    t = matmul(x, W)
    if b is None:
        return t

    y = t + b
    t.data = None  # Release t.data (ndarray) for memory efficiency
    return y


# =============================================================================
# activation function: sigmoid / relu / softmax / log_softmax / leaky_relu
# =============================================================================
class Sigmoid(Function):
    def forward(self, x):
        xp = cuda.get_array_module(x)
        # y = 1 / (1 + xp.exp(-x))
        y = xp.tanh(x * 0.5) * 0.5 + 0.5  # Better implementation
        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = gy * y * (1 - y)
        return gx


def sigmoid(x):
    return Sigmoid()(x)


def sigmoid_simple(x):
    x = as_variable(x)
    y = 1 / (1 + exp(-x))
    return y


def softmax_simple(x, axis=1):
    x = as_variable(x)
    y = exp(x)
    sum_y = sum(y, axis=axis, keepdims=True)
    return y / sum_y


class Softmax(Function):
    def __init__(self, axis=1):
        self.axis = axis

    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = x - x.max(axis = self.axis, keepdims = True)
        y = xp.exp(y)
        y /= y.sum(axis = self.axis, keepdims = True)
        return y

    def backward(self, gy):
        y = self.outputs[0]()
        gx = y * gy
        sumdx = gx.sum(axis = self.axis, keepdims = True)
        gx -= y * sumdx
        return gx
        
def softmax(x, axis = 1):
    return Softmax(axis)(x)


# =============================================================================
# loss function: mean_squared_error / softmax_cross_entropy / sigmoid_cross_entropy / binary_cross_entropy
# =============================================================================
class MeanSquaredError(Function):
    """
    MeanSquaredError Class

    Methods
    -------
    forward : Calculate a loss(called y_hat).
    backward : Perform back-prop using differentiation.
    """    
    def forward(self, x0, x1):
        diff = x0 - x1
        y = (diff ** 2).sum() / len(diff)
        return y

    def backward(self, gy):
        x0, x1 = self.inputs
        diff = x0 - x1
        gx0 = gy * diff * (2. / len(diff))
        gx1 = -gx0
        return gx0, gx1


def mean_squared_error(x0, x1):
    return MeanSquaredError()(x0, x1)


def mean_squared_error_simple(x0, x1):
    x0, x1 = as_variable(x0), as_variable(x1)
    diff = x0 - x1
    y = sum(diff ** 2) / len(diff)
    return y


def softmax_cross_entropy_simple(x, t):
    x, t = as_variable(x), as_variable(t)
    N = x.shape[0]

    p = softmax(x)
    p = clip(p, 1e-15, 1.0)
    log_p = log(p)
    tlog_p = log_p[np.arange(N), t.data]
    y = -1 * sum(tlog_p) / N
    return y


class SoftmaxCrossEntropy(Function):
    def forward(self, x, t):
        N = x.shape[0]
        log_z = utils.logsumexp(x, axis=1)
        log_p = x - log_z
        log_p = log_p[np.arange(N), t.ravel()]
        y = -log_p.sum() / np.float32(N)
        return y

    def backward(self, gy):
        x, t = self.inputs
        N, CLS_NUM = x.shape

        gy *= 1/N
        y = softmax(x)
        # convert to one-hot
        xp = cuda.get_array_module(t.data)
        t_onehot = xp.eye(CLS_NUM, dtype=t.dtype)[t.data]
        y = (y - t_onehot) * gy
        return y

def softmax_cross_entropy(x, t):
    return SoftmaxCrossEntropy()(x, t)


# =============================================================================
# max / min / clip
# =============================================================================
class Clip(Function):
    def __init__(self, x_min, x_max):
        self.x_min = x_min
        self.x_max = x_max

    def forward(self, x):
        xp = cuda.get_array_module(x)
        y = xp.clip(x, self.x_min, self.x_max)
        return y

    def backward(self, gy):
        x, = self.inputs
        mask = (x.data >= self.x_min) * (x.data <= self.x_max)
        gx = gy * mask
        return gx

def clip(x, x_min, x_max):
    return Clip(x_min, x_max)(x)



