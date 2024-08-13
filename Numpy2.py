#!/usr/bin/env python
# coding: utf-8

# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# In[1]:


#Print the shape of a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


# In[2]:


#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)


# In[4]:


# reshaping we can add or remove dimensions or change number of elements in each dimension.
#Convert the following 1-D array with 12 elements into a 2-D array.
#The outermost dimension will have 4 arrays, each with 3 elements:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
#always remaimber while shaping lets take example last element 3 is always  no. of consider coloum and 4 is no. of row and if one more no then it is no. of array
print(newarr)


# In[1]:


#Convert the following 1-D array with 12 elements into a 3-D array.
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)


# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
# 

# In[3]:


#Check if the returned array is a copy or a view:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2,4).base)


# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.
# 

# In[4]:



#Convert 1D array with 8 elements to 3D array with 2x2 elements:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)


# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# 
# We can use reshape(-1) to do this.
# 

# In[5]:



#Example
#Convert the array into a 1D array:
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

