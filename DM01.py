#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
random_no = random.sample(range(0,150),100)
print(random_no)
random_no.sort()
print(random_no)


# In[8]:


length = len(random_no)
mid = length//2


# In[9]:


bin1 = random_no[:mid]
print(bin1)


# In[15]:


bin2 = random_no[mid:]
print(bin2)


# In[16]:


bin1_mean = sum(bin1) / len(bin1)
bin1_m = int(bin1_mean)


# In[17]:


bin2_mean = sum(bin2) / len(bin2)
bin2_m = int(bin2_mean)


# In[30]:


print("Bin1: ",bin1_m)
print("Bin2: ",bin2_m)


# In[ ]:





# In[31]:


for n, i in enumerate(bin1):
    bin1 = bin1_m
print(bin1)


# In[ ]:




