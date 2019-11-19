#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_0 = {
    'username':'student1',
    'first_name':'Shareef',
    'last_name':'M'
    
}
print(user_0)


# In[7]:


for s,m in user_0.items():
    print(f"\nKey:{s}")
    print(f"\nvalue:{m}")


# In[8]:


for s in user_0.keys():
    print(f"key: {s}")


# In[9]:


for m in user_0.values():
    print(f"value: {m}")


# In[10]:


alien = {'color':'green','points':5}

print(alien)


# In[11]:


del alien['points']

print(alien)


# In[ ]:




