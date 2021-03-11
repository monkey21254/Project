import numpy as np
from myPackage.core_complex import Function
from myPackage.core_complex import as_variable
from myPackage import utils

from myPackage import Variable # line 324 (get_array_module)
gpu_enable = True
try:
    import cupy as cp
    cupy = cp
except ImportError:
    gpu_enable = False


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


class Sigmoid(Function):
    def forward(self, x):
        xp = get_array_module(x)
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


def get_array_module(x): # line 6 (import ...)
    """Returns the array module for `x`.
    Args:
        x (dezero.Variable or numpy.ndarray or cupy.ndarray): Values to
            determine whether NumPy or CuPy should be used.
    Returns:
        module: `cupy` or `numpy` is returned based on the argument.
    """
    if isinstance(x, Variable):
        x = x.data

    if not gpu_enable:
        return np
    xp = cp.get_array_module(x)
    return xp


