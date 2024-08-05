#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
import requests
#API to fetch temperature of city
city_name=input("Enter city name: ");
api_key='043f5170eef76df0fbf19f4ab2ca0003'
#To build URL api
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_information=requests.get(api_url)
print(get_server_information.json())


# In[ ]:




