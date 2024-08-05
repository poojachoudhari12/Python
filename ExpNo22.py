#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Data preproccessing  Tools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset=pd.read_csv('data.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:,-1].values
print(X)
print(y)


# In[ ]:




