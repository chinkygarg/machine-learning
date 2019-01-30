#!/usr/bin/env python
# coding: utf-8

# In[12]:


import seaborn as sns
import pandas as pd
import numpy as np
from numpy.random import randint


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[184]:


np.random.seed(100)
data_frame=pd.DataFrame(randint(6,7),['A','B','C','D','E','F'],['total_bill','tip','sex','smoker','date','time','size'])


# In[206]:


data_frame


# In[207]:


data_frame.insert(0,"team","123000")


# In[208]:


data_frame


# In[209]:


data_frame.reset_index()


# In[210]:


s


# In[211]:


sns.distplot(data_frame['total_bill'],kde=False,bins=40)#kde=kernel destination estimation


# In[212]:


sns.jointplot(x='total_bill',y='tip',data=data_frame,kind='kde')#hex is used for hexagonal image and reg for regression


# In[213]:


sns.pairplot(data_frame,hue='sex',palette='coolwarm') #pairing of all the blocks


# In[214]:


sns.rugplot(data_frame['total_bill'])


# In[215]:


sns.barplot(x='sex',y='total_bill',data=data_frame,estimator=np.std)


# In[216]:


sns.countplot(x='sex',data=data_frame)


# In[217]:


sns.boxplot(x='day',y='total_bill',data=data_frame,hue='smoke',)


# In[218]:


sns.violinplot(x='day',y='total_bill',data=data_frame,hue='sex',split=True)


# In[219]:


sns.stripplot(x='day',y='total_bill',data=data_frame,jitter=True,hue='sex',palette='Set1')


# In[220]:


sns.violinplot(x='day',y='total_bill',data=data_frame)
sns.swarmplot(x='day',y='total_bill',data=data_frame,color='black')


# In[221]:


sns.factorplot(x='day',y='total_bill',data=data_frame,kind='bar')


# In[222]:


#matrix plot


# In[223]:



data_frame1=pd.DataFrame(randint(5),['A','B','C','D','E'],['year','month','passengers'])
data_frame1


# In[242]:


flight= {'year':[1949,1949,1949,1949,1949,1987,1986,2012],'month':["january","feb","march","april","may","june","july","aug",],'passenger':[112,118,132,129,121,132,123,432]}#used to insert data into dataframe
data_frame1 =pd.DataFrame(flight)
data_frame1


# In[ ]:





# In[ ]:





# In[ ]:





# In[243]:


data_frame


# In[244]:


data_frame1


# In[245]:


data_frame1.corr()


# In[246]:


tc = data_frame.corr()
tc


# In[247]:


sns.heatmap(tc,annot=True)


# In[249]:


cp=data_frame1.pivot_table(index='month',columns='year',values='passenger')
cp


# In[255]:


sns.heatmap(cp,cmap='magma',linecolor='white',linewidths=3)


# In[265]:


sns.lmplot(x='total_bill',y='tip',data=data_frame)


# In[269]:


iris=pd.DataFrame(randint(5,5),['A','B','C','D','E'],['sepal_length','sepal_width','petal_length','petal_width','species'])
iris


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




