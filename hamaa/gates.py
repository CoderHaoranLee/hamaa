# encoding: utf-8
"""
@author: monitor1379 
@contact: yy4f5da2@hotmail.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: gates.py
@time: 2016/9/11 9:01

计算单元
"""

import numpy as np


class MulGate:
    """乘法单元"""

    @staticmethod
    def forward(w, x):
        return np.dot(x, w)

    @staticmethod
    def backward(w, x, d_z):
        d_w = np.dot(np.transpose(x), d_z)
        d_x = np.dot(d_z, np.transpose(w))
        return d_w, d_x


class AddGate:
    """专用于n*m维与1*m维的加法单元"""

    @staticmethod
    def forward(x, b):
        return x + b

    @staticmethod
    def backward(x, b, d_z):
        d_x = np.array(d_z)
        d_b = np.array(d_z)
        if b.shape[0] == 1:
            d_b = np.sum(d_b, axis=0, keepdims=True)
        if b.shape[1] == 1:
            d_b = np.sum(d_b, axis=1, keepdims=True)
        return d_x, d_b


class LinearGate:
    """线性计算单元"""

    @staticmethod
    def forward(x):
        return np.array(x)

    @staticmethod
    def backward(x, d_z):
        return np.ones_like(x) * d_z

class SigmoidGate:
    """sigmoid单元"""

    @staticmethod
    def forward(x):
        z = 1.0 / (1.0 + np.exp(-x))
        return z

    @staticmethod
    def backward(x, d_z):
        a = SigmoidGate.forward(x)
        d_x = a * (1 - a) * d_z
        return d_x


class TanhGate:
    """tanh单元"""

    @staticmethod
    def forward(x):
        e1 = np.exp(x)
        e2 = np.exp(-x)
        return (e1 - e2) / (e1 + e2)

    @staticmethod
    def backward(x, d_z):
        a = TanhGate.forward(x)
        d_x = (1 - a**2) * d_z
        return d_x


class ReLUGate:
    """relu单元"""
    @staticmethod
    def forward(x):
        z = np.array(x)
        z[z < 0] = 0
        return z

    @staticmethod
    def backward(x, d_z):
        d_x = np.ones_like(x)
        d_x[x < 0] = 0
        return d_x * d_z


class Conv2DGate:

    @staticmethod
    def forward():
        pass

    @staticmethod
    def backward():
        pass


class MaxPooling2DGate:
    @staticmethod
    def forward():
        pass

    @staticmethod
    def backward():
        pass


class MeanPooling2DGate:
    @staticmethod
    def forward():
        pass

    @staticmethod
    def backward():
        pass