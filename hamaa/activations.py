# encoding: utf-8
"""
@author: monitor1379 
@contact: yy4f5da2@hotmail.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: activations.py
@time: 2016/10/9 20:29


"""

from .gates import SigmoidGate, TanhGate, ReLUGate


_dict = {'sigmoid': SigmoidGate,
         'tanh': TanhGate,
         'relu': ReLUGate,
         }


def get(identifier):
    return _dict.get(identifier)
