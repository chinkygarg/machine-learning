#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
step =0

print("this",num)
for i in range(1,11): 
    num = np.random.randint(1,7)
    if(num <=3)and (step!=0):
        print("level0")
        step -=1
    if(num<=5):
        step +=1
    if(num==6):
        n = np.random.randint(1,7)
        print("new",n)
        step =step+n
print("count:",count)
print("step:",step)
        
        
    
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




