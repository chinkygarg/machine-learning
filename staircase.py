#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import random
a=[]
list1= [1,2,3,4,5,6]
for i in range(1,11): 
    step =0
    num = np.random.choice(list1,p=[1/4,1/4,1/4,1/12,1/12,1/12])
    if num <4 and step!=0:
        step -=1
    if num>=4 or num<6:
        step =step+1
    if num==6:
        n = np.random.choice(list1,p=[1/4,1/4,1/4,1/12,1/12,1/12])
        step =step+n
        
        a.append(step)
        
print(step)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




