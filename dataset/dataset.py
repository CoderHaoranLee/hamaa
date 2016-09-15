# encoding: utf-8
"""
@author: monitor1379 
@contact: yy4f5da2@hotmail.com
@site: www.monitor1379.com

@version: 1.0
@license: Apache Licence
@file: dataset.py
@time: 2016/9/11 9:00

数据集加载文件
"""

import numpy as np
import sklearn.datasets
from mnist import mnist_decoder
import os

def load_or_data():
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 1])
    return x, y


def load_and_data():
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])
    return x, y


def load_xor_data():
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    return x, y


def load_moons_data(nb_data, noise):
    return sklearn.datasets.make_moons(nb_data, noise=noise)


def load_mnist_data(nb_training, nb_test):
    training_x = mnist_decoder.load_train_images(num_data=nb_training)
    training_y = mnist_decoder.load_train_labels(num_data=nb_training)
    test_x = mnist_decoder.load_test_images(num_data=nb_test)
    test_y = mnist_decoder.load_test_labels(num_data=nb_test)
    return training_x, training_y, test_x, test_y

