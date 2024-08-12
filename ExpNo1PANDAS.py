#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pandas example
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 


# In[2]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df) 


# In[3]:


import pandas as pd

print(pd.options.display.max_rows) 


# In[4]:


import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 


# In[6]:


import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 


# In[7]:


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

