# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 23:37:02 2020

Problem Set 06 Solutions

@author: Blin
"""
import numpy as np

# 1) 
print('Question 1)')

def ReLU(x):
    return x * (x > 0)

X1 = np.array([1, 0, -1])
X2 = np.array([1, 0, 10])
X3 = np.array([-1, 0, -10])

print('ReLU for [1,0,-1] ', ReLU(X1))
print('ReLU for [1,0,10] ', ReLU(X2))
print('ReLU for [-1,0,-10] ', ReLU(X3))

# 2) 
print('Question 2)')

def affine(X, W, b):
    return np.sum((np.matmul(X, W), b), axis=0)

b = np.array([[1, -1, 0]])
W = np.array([[2, 0, 0],[0, 2, 0]])
X1 = np.array([[1, 1],[0, -1]])
X2 = np.array([[1, 0],[1, -1]])
X3 = np.array([[1, 1],[1, 1]])

print('Affine layer for [1,1][0,-1] \n', affine(X1, W, b)) 
print('Affine layer for [1,1][0,-1] \n', affine(X2, W, b)) 
print('Affine layer for [1,1][0,-1] \n', affine(X3, W, b)) 

# 3) 
print('Question 3)')
# batch softmax function from last week
def BatchS(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1)[:, np.newaxis]
# step 1 -> init data
X = np.array([[1,1],[0,-1]])
W1 = np.array([[2,0,0],[0,2,0]])
b1 = np.array([[1,-1,0]])
W3 = np.array([[4,0],[0,-1],[0,-1]])
b3 = np.array([[1,-1]])
print('Input Data \n', X)
# step 2 -> affine layer
affined_data = affine(X, W1, b1)
print('Data after affine layer \n', affined_data)
# step 3 -> ReLU
rectified_data = ReLU(affined_data)
print('Data after ReLU \n', rectified_data)
# step 4 -> affine layer
affined_data_02 = affine(rectified_data, W3, b3)
print('Data after affine layer two \n', affined_data_02)
# step 5 -> softmax
softmax_data = BatchS(affined_data_02)
print('Data after soft max \n', softmax_data)