# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:25:25 2019

Reogranizing arrays 

@author: Blin
"""

import numpy as np

# reshaping
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(before.shape)

# always same amount of values, 4,2 / 2,2,2 / 8,1 etc.
after = before.reshape((8,1))
print(after)

# vertical stacking 
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2]))
print(np.hstack([v1,v2]))

# boolean masking and advanced indexing
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr > 2)
print(arr == 1)
print(arr[arr > 2]) # gets only the remaining data

arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1[[1,2,8]])

bebe = arr > 2
print(arr[bebe]) 

# check if any value is higher than 8 in rows
print(np.any(arr1 > 8, axis = 0))

# check if all value is higher than 8 in rows
print(np.all(arr1 > 8, axis = 0))

mask = (arr1 > 2) & (arr1 < 4)
print(arr1[mask])