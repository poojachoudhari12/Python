#!/usr/bin/env python
# coding: utf-8

# #Data types in Numpy
# Below is a list of all data types in NumPy and the characters used to represent them.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# 

# In[1]:


#Get the data type of an array object:
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)


# In[2]:


#Create an array with data type string:
#For i, u, f, S and U we can define size as well.
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


# In[ ]:


#Create an array with data type 4 bytes integer:

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)


# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# A non integer string like 'a' can not be converted to integer (will raise an error):
# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

# In[3]:


#Change data type from float to integer by using 'i' as parameter value:

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


# In[4]:


#Change data type from float to integer by using int as parameter value:

import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)


# In[5]:


#Change data type from integer to boolean:

import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)


# NumPy Array Copy vs View
# the copy is a new array, and the view is just a view of the original array.
# 
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# In[6]:


#Make a copy, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# In[7]:


#Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# 
# Every NumPy array has the attribute base that returns None if the array owns the data.
# 
# Otherwise, the base  attribute refers to the original object.

# In[8]:


#Print the value of the base attribute to check if an array owns it's data or not:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

