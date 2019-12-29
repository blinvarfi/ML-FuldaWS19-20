"""
Created on Sat Dec 28 23:13:25 2019

Problem Set 02 Solutions

@author: BlinVarfi, fdai6433.
"""

import numpy as np;

# get mnist dataset
traind, testd, trainl, testl = np.load('../data/mnist.npz', 'rb').values();

# 1.a) 
print('\nQuestion 1.a)')
print('Samples (traind) shape: ', traind.shape)
print('Target values (trainl) shape: ', trainl.shape)
print('Number of samples: ', traind.shape[0])
print('Number of targets: ', trainl.shape[0])
print('Numbers that make a sample: ', traind[0].size)
# each of 10 dimensions for the targets corresponds to the numbers from 0-9.

# 1.b)
print('\nQuestion 1.b)')
sample1000 = traind[999]
target1000 = trainl[999]
print('Sample 1000 has a class of: ', np.argmax(target1000))

# 1.c)
print('\nQuestion 1.c)')
# take the index of min max through each row and will return a vector from
# where we can retrieve the min max number.
lowestClass = np.min(np.argmin(trainl, axis = 1))
highestClass = np.max(np.argmax(trainl, axis = 1))
print('Lowest class is: ', lowestClass)
print('Highest class is: ', highestClass)

# 1.d)
print('\nQuestion 1.d)')
equalFive = np.argmax(trainl, axis = 1) == 5
numOfFives = np.sum(trainl[equalFive])
print('Total number of targets with value 5 is: ', numOfFives)

# 1.e)
print('\nQuestion 1.e)')
sample10 = traind[9]
minPx = np.min(sample10)
maxPx = np.max(sample10)
print('Mininum pixel value of sample ten: ', minPx)
print('Maximum pixel value of sample ten: ', maxPx)

# 1.f)
print('\nQuestion 1.f)')
# start slicing from second row and take every two rows into the new array
everyNdRow = sample10[1::2, ::]
print('Shape of every two rows: ', everyNdRow.shape)
# start slicing from second col and take every two cols into the new array
everyNdCol = sample10[::, 1::2]
print('Shape of every two columns: ', everyNdCol.shape)
# inverted rows and cols
mirroredRowsCols = sample10[::-1, ::-1]
# copy sample10 to another array
cp_s10 = np.copy(sample10)
# get the sum over each column, from where select top 10 indexes 
topTenCols = (np.sum(-cp_s10, axis = 0)).argsort()[:10]
cp_s10[::, topTenCols] = 0
print('Top 10 columns: ', topTenCols)
# copy sample10 to another array
cp1_s10 = np.copy(sample10)
# get the sum over each column, from where select lowest 10 indexes 
lowestTenCols = (np.sum(cp1_s10, axis = 0)).argsort()[:10]
cp1_s10[::, lowestTenCols] = 0
print('Lowest 10 columns: ', lowestTenCols)
# invert rows and cols, take only 2nd rows and cols.
ultimateSlicing = sample10[::-1,::-1][1::2,1::2]
print('Shape of ultimate slicing: ', ultimateSlicing.shape)

# 1.g)
print('\nQuestion 1.g)')
maskFour = np.argmax(trainl, axis = 1) == 4
targetsClassFour = trainl[maskFour]
samplesClassFour = traind[maskFour]
print('Shape of class four samples is: ', samplesClassFour.shape)
print('Shape of class four targets is: ', targetsClassFour.shape)

# 1.h)
print('\nQuestion 1.h)')
maskFourOrNine = (np.argmax(trainl, axis = 1) == 4) | (np.argmax(trainl, axis = 1) == 9)
targetsClassFourOrNine = trainl[maskFourOrNine]
samplesClassFourOrNine = traind[maskFourOrNine]
print('Shape of class four samples is: ', samplesClassFourOrNine.shape)
print('Shape of class four targets is: ', targetsClassFourOrNine.shape)

# 1.i)
print('\nQuestion 1.i)')
first10000Samples = traind[:10000]
first10000Targets = trainl[:10000]
print('Shape of first 10000 samples is: ', first10000Samples.shape)
print('Shape of first 10000 targets is: ', first10000Targets.shape)

# 1.j)
print('\nQuestion 1.j)')
traind = 1 - traind
print('Getting the total sum for testing purposes: ', np.sum(traind))

# 1.h)
print('\nQuestion 1.h)')
indexes = np.random.randint(low = 0, high = 59999, size = 10000)
print('Random selected indexes: ', indexes)
cp = np.copy(traind[indexes])

