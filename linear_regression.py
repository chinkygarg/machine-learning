#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.linspace(-10,10,200)
x


# In[3]:


e = np.random.randn(200)
e


# In[4]:


m = 2


# In[5]:


c=4


# In[6]:


y = m*x+c+e*2
y


# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


plt.scatter(x,y)


# In[9]:


m1 = np.random.randint(1,100)
m1


# In[10]:


c1 = np.random.randint(1,100)
c1


# In[11]:


y1 = m1*x+c1


# # 

# In[12]:


y1


# In[13]:


error=y-y1
error


# In[14]:


np.dot(error,x)


# In[15]:


m1 = m1-(-1/200)*np.dot(error,x)
m1


# In[16]:


c1 = c1-(-1/2*200)*np.sum(error)
c1


# # 

# In[17]:


m1 = m1-(0.01)
m1


# In[18]:


mse = (1/200)*np.sum(np.square(error))
mse


# In[19]:


cost = 1/200*np.sum(y-y1)
cost


# 

# 

# In[33]:


m=0
c=0
list1=[]
for i in range (1,2000):
    y1 = (m1*x)+c1
    z = y-y1 
    mse = (1/200)*np.sum(np.square(error))
    list1.append(mse)
    m1=m1+(0.01*(1/100*(np.dot(z,y))))
    c1=c1+(0.01*(1/100*(np.sum(z))))


# In[34]:


print(m1,c1)
y1=(m1*x)+c1


# In[ ]:




