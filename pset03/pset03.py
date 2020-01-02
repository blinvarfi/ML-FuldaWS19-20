# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:57:15 2019

Problem Set 03 Solutions

@author: BlinVarfi, fdai6433.
"""

from matplotlib import pyplot as plt
import numpy as np

# get mnist dataset
traind, testd, trainl, testl = np.load('../data/mnist.npz', 'rb').values();
TOTAL_SAMPLES = 60000

# customizing matplotlib
plt.style.use('dark_background') 

# 1.a) 
print('Question 1.a)')
# real matrix multiplication using np.dot 
sample_arr01 = np.array([[2,4],[8,9]])
sample_arr02 = np.array([[3,3],[5,6]])
arr_multiplication = np.dot(sample_arr01, sample_arr02)
#arr_multiplication = np.matmul(sample_arr01, sample_arr02)
print('The product of ', sample_arr01, ' X ', sample_arr02, ' = ', arr_multiplication)

# 1.b) 
print('\nQuestion 1.b)')
test_arr01 = np.array([2,3,4])
print('Current shape of test array: ', test_arr01.shape, 'can\'t perform mult.')
test_arr01 = test_arr01[np.newaxis, :]
test_arr01 = np.append(test_arr01, [[1,2,3]], axis=0)
print(test_arr01) 
print('New shape of test array: ', test_arr01.shape)
print(np.dot(sample_arr01, test_arr01))

# 1.c) 
print('\nQuestion 1.c)')
broadcasting_example = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print('Old shape: ', broadcasting_example.shape)
broadcasting_example = broadcasting_example[:,np.newaxis,:]
print('New shape: ', broadcasting_example.shape)

# 2.a) 
print('\nQuestion 2.a)')
#pixel_mean = np.mean(traind, axis = 0)
pixel_mean = np.sum(traind, axis = 0) / TOTAL_SAMPLES
fig, ax = plt.subplots()
ax.set_title('Average Image')
ax.imshow(pixel_mean)
plt.show()

# 2.b)
print('\nQuestion 2.b)')
pixel_variance = np.sum((traind - pixel_mean)**2, axis=0) / TOTAL_SAMPLES 
fig, ax = plt.subplots()
ax.set_title('Variance')
ax.imshow(pixel_variance)
plt.show()

# 2.c)
print('\nQuestion 2.c)')
pixel_std_deviation = pixel_variance ** (1/2)
fig, ax = plt.subplots()
ax.set_title('Standard Deviation')
ax.imshow(pixel_std_deviation)
plt.show()

# 2.d)
print('\nQuestion 2.d)')
first_500 = traind[0:500]
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
fig.suptitle('Histograms')
ax[0].set_ylabel('Number of pixels')
ax[1].set_ylabel('Number of pixels')
ax[1].set_xlabel('Darkness of a pixel (0, 1)')
ax[0].hist(first_500[:,13,13], color='y')
ax[1].hist(first_500[:,0,0])
plt.show()

# 2.e)
print('\nQuestion 2.e)')
# WEIRD QUESTION, WHAT DOES THIS EVEN MEAN. WHY?
sample_min = np.min(traind, axis=(1,2));
sample_max = np.max(traind, axis=(1,2));

# 2.f)
print('\nQuestion 2.f)')
print('The image will show white for all pixels that are NEVER used, and grey' +
      'or black for pixels used at least once.')
pixel_max = np.max(traind, axis=0);
fig, ax = plt.subplots()
ax.set_title('Max value for each pixel')
ax.imshow(pixel_max)
plt.show()

# 3.a)
print('\nQuestion 3.a)')
sample_500 = traind[499]
flatten_arr = sample_500.reshape(1, -1)
#outer product = v*vT
#outer_prod = np.dot(flatten_arr.reshape(28*28, 1), flatten_arr)
outer_prod = flatten_arr.reshape(28*28, 1) * flatten_arr
print('Shape of outer product is: ', outer_prod.shape)
fig, ax = plt.subplots()
ax.set_title('Sample 500 outer product')
ax.imshow(outer_prod)

# 3.b)
print('\nQuestion 3.b)')
first_1000 = traind[0:1000]
flatten_1000 = first_1000.reshape(1000, 28*28)
print(flatten_1000.shape)
print(flatten_1000.reshape(28*28, 1000).shape)
#outer product = v*vT
outer_prod02 = np.mean(flatten_1000[:,np.newaxis,:] * flatten_1000[:,:,np.newaxis], axis=0)
print(outer_prod02.shape)

# 3.c)
print('\nQuestion 3.c)')
eigh_val, eigh_vec = np.linalg.eigh(outer_prod02)f
ev_1 = eigh_vec[:,-1].reshape(28, 28)
ev_2 = eigh_vec[:,-2].reshape(28, 28)
fig, ax = plt.subplots(2, 1)
fig.suptitle('First and Second EigenVectors')
ax[0].imshow(ev_1)
ax[1].imshow(ev_2)
plt.show()






