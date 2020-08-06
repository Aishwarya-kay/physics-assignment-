#!/usr/bin/env python
# coding: utf-8

# In[8]:


# prepare a list of five elements and slice it to index 3
List = [1, 2, 3, 4, 5] 
s = slice(3) 
print('list after slicing')
print(List[s])


# In[26]:


#Prepare a list of 8 elements and slice it from index 2 to index 6
list=[1,2,3,4,5,6,7,8]
s=slice(2,6)
print(list[s])


# In[36]:


# prepare a list and use if-else statement and print
list=[1,2,3,-4,0]
for a in list:
    if (a>0):
        print(a)
    else:
        print('lesser than 0')


# In[42]:


#Prepare a multiple list using if-else statement
list=[1,2]
list1=[6,7]
for a in list:
    for b in list1:
        if (b>a):
            print('greater')
        else:
            print('lesser')


# In[61]:


#prepare a empty dictionary and in the same program add key-value to it
dict={}
dict[1]='my'
dict[2]='name'
dict[3]='is'
dict[4]='raj'

print(dict)


# In[94]:


# Use if-else in dictionary
dict={1: 'my', 2: 'name', 3: 'is', 4: 'raj'}
dict1={1: 'MY', 2: 'NAME', 3: 'IS', 4: 'RAJ'} 
if (dict==dict1): 
    print('yes')
else:
    print('no')


# In[ ]:





# In[ ]:




