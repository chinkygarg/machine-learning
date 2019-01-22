#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[3]:


a=np.ones(10)


# In[4]:


a


# In[5]:


a*5


# In[6]:


b = np.arange(10,51)


# In[7]:


b


# In[8]:


c = np.arange(10,51,2)


# In[9]:


c


# In[10]:


d = [[1,2,3],[4,5,6],[7,8,9]]


# In[11]:


np.array(d)


# In[12]:


np.eye(1)


# In[13]:


np.eye(3,3)


# In[14]:


np.random.rand(1)


# In[15]:


np.random.randn(25)


# In[16]:


(np.arange(100).reshape(10,10)+1)/100


# In[17]:


np.linspace(0,1,20)


# In[18]:


mat = np.arange(1,26).reshape(5,5)


# In[19]:


mat


# mat[3:]

# In[20]:


mat[2:,1:]


# 

# 

# In[21]:


mat[3] [4]


# In[22]:


mat[:3,1:2]


# In[23]:


mat[4]


# In[24]:


mat[3:]


# In[25]:


np.sum(mat)


# In[26]:


np.std(mat)


# In[27]:


np.sum(mat,axis=0)


# In[28]:


np.sum(mat,axis=1)


# In[ ]:




