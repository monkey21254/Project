import numpy as np


class Optimizer:
    """
    Optimizer class
    
    Args
    ----
    target: This is optimized by hooks(func).
    hooks: There is option list including preprocessing params.

    Methods
    -------
    setup: This exists for update target.
    update: This exists for update params.
    """
    def __init__(self):
        self.target = None
        self.hooks = []

    def setup(self, target):
        self.target = target
        return self

    def update(self):
        # None 이외의 매개변수 리스트에 모으기
        params = [p for p in self.target.params() if p.grad is not None]

        # 전처리(옵션)
        for f in self.hooks:
            f(params)

        # 매개변수 갱신
        for param in params:
            self.update_one(param)

    def update_one(self, param):
        raise NotImplementedError()

    def add_hook(self, f):
        self.hooks.append(f)


class SGD(Optimizer):
    def __init__(self, lr=0.01):
        super().__init__()
        self.lr = lr

    def update_one(self, param):
        param.data -= self.lr * param.grad.data


class MomentumSGD(Optimizer):
    def __init__(self, lr = 0.01, momentum = 0.9):
        super().__init__()
        self.lr = lr
        self.momentum = momentum
        self.vs = {}

    def update_one(self, param):
        v_key = id(param)
        if v_key not in self.vs:
            self.vs[v_key] = np.zeros_like(param.data)

            v = self.vs[v_key]
            v *= self.momentum
            v -= self.lr * param.grad.data
            param.data += v


# class AdaGrad(Optimizer):
#     def __init__(self, lr = 0.001, eps = 1e-8):
#         super().__init__()
#         self.lr = lr
#         self.eps = eps
#         self.hs = {}

