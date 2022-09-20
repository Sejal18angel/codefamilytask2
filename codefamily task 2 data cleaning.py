#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/50_Startups.csv")


# In[3]:


df.corr()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[ ]:




