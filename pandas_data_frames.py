#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from numpy.random import randn


# In[4]:


np.random.seed(100)


# In[5]:


data_frame=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[6]:


data_frame


# In[7]:


data_frame['X']


# In[8]:


type(data_frame['W'])


# In[9]:


data_frame[['W','X']]


# In[10]:


data_frame['new'] = data_frame['Y']+ data_frame['X']


# In[11]:


data_frame


# In[12]:


data_frame.drop('new',axis=1,inplace=True)


# In[13]:


data_frame


# In[14]:


data_frame.drop('E',axis=0)


# In[15]:


data_frame.shape


# In[16]:


data_frame[['X','Y']]


# In[17]:


data_frame.loc['B']


# In[18]:


data_frame.iloc[2]


# In[19]:


data_frame.loc['B','Y']


# In[20]:


data_frame.loc[['A','B'],['W','X']]


# In[21]:


data_frame>0


# In[22]:


booldata_frame=data_frame>0


# In[23]:


data_frame[booldata_frame]


# In[24]:


data_frame[data_frame>0]


# In[25]:


data_frame['X']>0


# In[26]:


result=data_frame[data_frame['W']>0]

result
# In[27]:


result['Y']


# In[28]:


data_frame[data_frame['W']>0][['Y','X']]


# In[29]:


boolser = data_frame['W']>0


# In[30]:


boolser


# In[39]:


data_frame[(data_frame['W']>0) | (data_frame['Y']>1)]


# In[ ]:





# In[40]:


data_frame['W']>0


# In[42]:


data_frame.reset_index()


# In[43]:


newind = 'CA NY WY OR CO'.split()


# In[45]:


newind


# In[47]:


data_frame['States']=newind


# In[48]:


data_frame


# In[52]:


data_frame.set_index('States')


# In[54]:


outside =['G1','G1','G1','G2','G2','G2']
inside =[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.form_tuples(hier_index)


# In[ ]:




