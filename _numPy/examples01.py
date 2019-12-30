# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:51:41 2019

Basic np array initializations and functionalities.

@author: Blin
"""

import numpy as np

# 1D array, specifying data type
a = np.array([1,2,3], dtype='int16')
print('Array A: ', a)

# 2D array
b = np.array([[9.0, 8.0, 7.0],[6.0, 5.0, 4.0]])
print('Array B: ', b)

# get dimension
print('A dimensions: ',a.ndim, '\nB dimensions: ', b.ndim)

# get shape 
print('A shape: ',a.shape, '\nB shape: ', b.shape)

# get type
print('A type: ', a.dtype)
print('B type: ', b.dtype)

# get number of size in bytes per item
print('A item size: ', a.itemsize)
print('B item size: ', b.itemsize)

# get total number of items
print('A total size: ', a.size)
print('B total size: ', b.size)

# get total size - following two lines should be equal
print('A total size: ', a.nbytes)
print('A total size: ', a.size * a.itemsize)

# indexing 
c = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print('Array C: ', c)

# get specific elemnt [row, col]
print('[1,5] :', c[1,5] )
print('[-1, 3] :', c[-1,3])

# get a specific row / col
print('First row: ', c[0, :])
print('First col: ', c[:, 0])

# fancier slicing [startIndex:endIndex:stepSize]
print('First row specified ', c[0, 1:6:2])

# change a value
c[1,5] = 20
print('New Array C: ', c);

# change a column 
c[:,2] = 5
c[:,4] = [21, 31]
print('New Array C: ', c);

# 3d example
d = np.array([
        [[1,2],[3,4]],
        [[5,6],[7,8]]
    ])
print('Array D: ', d)

# get element (work outside in)
print('Element: ', d[0,1,0])

# replace
d[:,1,:] = [[9,9],[8,8]]
print('New Array D: ', d)

# init all 0s matrix 
e = np.zeros((2,3,4,5))
print('Array E: ', e);

# init all 1s matrix 
f = np.ones((4,2,2), dtype='int32')
print('Array F: ', f)

# init dynamic numbers matrix 
g = np.full((2,2), 99, dtype='float32')
print('Array G: ', g) 

# make like array A
h = np.full_like(a, 4)
print('Array H: ', h)

# init rand matrix (between zero and one)
i = np.random.rand(4,2,5)
print('Array I:\n', i)
j = np.random.random_sample(a.shape)
print('Array J:\n', j)

# init random integers 
k = np.random.randint(7, size=(3,3))
print('Array K:\n', k)

# identity matrix 
x = np.identity(5)
print('Array X:\n', x)

# repeat - axis 0 means rows.
z = np.array([[1,2,3],[4,5]])
r1 = np.repeat(z, 3, axis=0)
print('Repeatition: ', r1)

# Excercise 
arr = np.ones((5,5), dtype='int32')
arr[1:-1, 1:-1] = 0
arr[2,2] = 9
print('Solution: \n', arr)

# Array copying BE CAREFUL
arr01 = np.array([1,2,3])
#arr02 = arr01 this points to arr01
arr02 = arr01.copy() # the right way to do it
arr02[0] = 100
print(arr01)



