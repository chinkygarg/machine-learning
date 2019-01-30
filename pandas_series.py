#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


labels = ['a','b','c']
my_data = [10,20,30]
arry = np.array(my_data)
d = {'a':10,'b':20,'c':30}


# In[5]:


pd.Series(data=my_data)


# In[6]:


pd.Series(data=my_data,index=labels)


# In[7]:


pd.Series(my_data,labels)


# In[8]:


pd.Series(arry,labels)


# In[9]:


pd.Series(data =(sum,print,len))


# In[10]:


ser = pd.Series([1,2,3,4],['USA','Germany','Italy','Japan'])
ser


# In[11]:


ser2 = pd.Series([1,2,5,4],['USA','Germany','USSR','Japan'])
ser2


# In[12]:


ser+ser2


# In[ ]:




