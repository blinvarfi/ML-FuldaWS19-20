# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 23:45:42 2019

Math with np arrays.

@author: Blin
"""

import numpy as np

# basic arithmetics (element wise)

a = np.array([[1,2,3],[4,5,6]])
print(a - 1)
print(a * 2)
print(a / 5)

b = np.array([1,2,5])

print(a+b)
print(np.sin(a))
print(np.cos(b))

# linear algebra

arr1 = np.ones((2,3))
arr2 = np.full((3,2), 2)

print(np.matmul(arr1, arr2))

# statistics

stats = np.array([[1,2,3],[4,5,6]])

# same for max
print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))