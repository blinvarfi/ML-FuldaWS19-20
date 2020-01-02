# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 03:34:54 2020

Problem Set 05 Solutions

@author: Blin
"""
import numpy as np

# 3) 
print('Question 3)')

def S(x):
    return np.exp(x) / np.sum(np.exp(x))

print('Softmax for [-1, -1, 5] ', S(np.array([-1, -1, 5])))
print('Softmax for [1, 1, 2] ', S(np.array([1, 1, 2])))

# 4) 
print('Question 4)')
    
def CE(x, t):
    return  -1 * np.sum(t * np.log(x))

t = np.array([0,0,1])

print('CE for x1 ', CE(np.array([0.1,0.1,0.8]), t))
print('CE for x2 ', CE(np.array([0.3,0.3,0.4]), t))
print('CE for x3 ', CE(np.array([0.8,0.1,0.1]), t))

# 5) 
print('Question 5)')
# main idea is to avoid complecity of computation we create batches of data instead,
# so here we need to find some kind of an average over a number of batches rather than
# one big vector.    
def BatchS(x):
    return np.exp(x) / np.sum(np.exp(x), axis=1)[:, np.newaxis]

def BatchCE(x, t):
    return  -1 * np.sum(np.sum(t * np.log(x))) / x.shape[0]

x1 = np.array([[-1,-1,5],[1,1,2]]) ; 
#print('exp test: ', np.exp(x1))
#print('exp test: ', np.sum(np.exp(x1), axis=1)[:, np.newaxis])
t2 = np.array([[0,0,1],[0,0,1],[ 0,0,1]]) ;
x2 = np.array([[0.1,0.1,0.8],[0.3,0.3,0.4],[ 0.8,0.1,0.1]]) ; 

print("Batch softmax", BatchS(x1)) ;
print("Batch CE", BatchCE(x2,t2)) ;

