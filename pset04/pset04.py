# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 04:28:56 2020

@author: Blin
"""
from matplotlib import pyplot as plt
import numpy as np

traind, testd, trainl, testl = np.load('../data/mnist.npz', 'rb').values();

# customizing matplotlib
plt.style.use('dark_background') 

# 3) 
print('Question 3)')

def f(x):
    return np.array(x[0]**2, 2*x[1]**2)

def grad_f(x):
    return np.array([2*x[0], 4*x[1]])

def calc_steps(x, n, step):
    for i in range(1, n):
        x = x - step * grad_f(x)
        print('Step ', i, ' value is ', x)
        
calc_steps(np.array([1, 3]), 6, 0.1)

# 4)
# BIG QUESTION MARK ABOUT THIS SOLUTION 
print('Question 4)')
first_500 = traind[0:500].reshape(500, 784)
cov_matrix = np.cov(first_500, rowvar=False)
eigh_val, eigh_vec = np.linalg.eigh(cov_matrix)
print('Covariance matrix shape ', cov_matrix.shape)
fig, ax = plt.subplots(1, 10)
fig.suptitle('First 5 and Last 5 EigenVectors')
for i in range (0, 10):
    ax[i].imshow(eigh_vec[:,i-5].reshape(28, 28))
plt.show()

# 5.a)
print('Question 5.a)')
first_500 = traind[0:500].reshape(500, 784)
op_500 = np.mean(first_500[:,np.newaxis,:] * first_500[:,:,np.newaxis], axis=0)
eigh_val, eigh_vec = np.linalg.eigh(op_500)
transformed_500 = np.dot(first_500, eigh_vec)
print('Shape of first 500 elements transformed ', transformed_500.shape)
# 5.b)
print('Question 5.b)')
transformed_500[:,0:-5] = 0
# 5.c)
print('Question 5.c)')
transformed_500_2 = np.dot(transformed_500, np.transpose(eigh_vec))
print(transformed_500_2.shape)
fig, ax = plt.subplots(1, 3)
fig.suptitle('First 3 samples')
for i in range (0, 3):
    ax[i].imshow(transformed_500_2[i].reshape(28,28))
plt.show()