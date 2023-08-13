#!/usr/bin/env python
# coding: utf-8

# Variable Name

# There are several techniques you can used to make valiables
# 1. Camel Case : In camel case first word should be initilized with samll letter and second letter is initilized with spectial letter and thirt letter initilized with samll letter and follow the hump structure 

# In[3]:


myHappyday = "07"


# 2.Pascal Case : In a pascal cse each and every word satrt with the capital letter 

# In[4]:


MyHappyDay = "08"


# 3.Snake Case : Each word is seprated by '_' character 

# In[5]:


my_happy_day="09"


# Casting : Variable Type 

# In[6]:


a,b,c="Archit","Somanath","Siddhi"


# In[7]:


a


# In[8]:


b


# In[9]:


c


# In[10]:


d=e=f="Arvi"


# In[11]:


e


# In[12]:


f


# In[13]:


d


# In[14]:


bazaar=['Fruits','Sugar','Rice','Eggs']


# In[18]:


j,k,l,m=bazaar #convert list in variable


# In[16]:


k


# In[19]:


m


# List UnPack

# In[20]:


animals = ['snake','elephant','frog','worm','Mud Frog']


# In[21]:


reptilise, memmal ,*amphibians=animals #to store multiple varibale we use *


# In[22]:


amphibians


# In[23]:


type(reptilise)


# In[24]:


reptilise


# In[25]:


type(amphibians)


# In[26]:


food = ['Apple','Ginger','Garlic','Cumin','Fish']


# In[29]:


fruit,*veg,non_veg=food


# In[30]:


non_veg


# In[31]:


veg


# Cocatination 

# 

# globle Variable : 1.are the varibale whiche created outside of the function
# 2. Used by both inside of the fuction and outside of the function

# In[45]:


x= "Iphone"

def myfun():
    x="Android"
    print("My New Phone is " + x)
    
myfun()    


# Local Variable : 1. Are the varibales which created inside of the function. This varibale is aasesable within a function

# In[46]:


x= "Iphone"

def myfun():
    x="Android"
    print("My New Phone is " + x)
    
myfun()

print("My New Phone is " + x)


# In[ ]:




