#!/usr/bin/env python
# coding: utf-8

# # Variable Names

# A variable name must start with a letter or the underscore character.
# A variable name cannot start with a number.
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# There are several are techniques you can used to create variables 
# 1. Camel case : In camel case first word is intialized with small letter and
# second word is intialized with capital letter and 
# third word is intialized with again small letter
# and follow the hump like structure.

# In[2]:


myHappyday = 7
print(myHappyday)


# 2.pascal case  : Each word start with a capital letter.

# In[3]:


MyHappyDay = "Siddhi"
print(MyHappyDay)


# 3.Snake Case :Each word is separated by underscore(_) Character.

# In[4]:


my_happy_day = "Siddhi"
print(my_happy_day)


# Casting

# In[5]:


a=1
b=2.4
c='DSAI'


# In[6]:


print(type(a))
print(type(b))
print(type(c))


# In[8]:


a,b,c = 'DSAI','5','#@$'
print(a)
print(b)
print(c)


# In[9]:


a=b=c = "DSAI" # valeues_over_write
print(a)
print(b)
print(c)


# In[11]:


Bazzar = ['Fish','Fruits',"Cheese","Butter"] #list
print(Bazzar)


# In[13]:


a,b,c,d = Bazzar  #list
print(a)
print(b)
print(c)
print(d)


# In[14]:


Animals = ['Snake','Elephant','Frog','Worm','Mud Frog'] #list unpack


# In[15]:


raptiles,mammals,amphibiance = Animals


# In[16]:


raptiles,mammals,*amphibiance = Animals #astrik is use  to pack many value to one varibles


# In[17]:


print(raptiles)
print(mammals)
print(amphibiance)


# In[18]:


print(type(mammals))
print(type(amphibiance))


# In[19]:


food = ['apple','ginger','garlic','cumin','fish']


# In[20]:


fruit,*vegitables,non_veg=food #to break list add varible ahead of it.
print(fruit)
print(vegitables)
print(non_veg)


# # Concatination

# Global variable are the variables which created outside of the function .
# Global variable can be use by every one, both inside of the function and out side of the function.

# In[21]:


a="DSAI"

def msc():
    a="CS"
    #print(" class: \n" +a)
msc()
print(" class:"+a)


# local variable : They are the variables which created inside the function and this variable will be accessable with in the function.

# In[22]:


a="DSAI"

def msc():
    a="CS"
    print(" class: " +a)
msc()
#print(" class: \n"+a)


# In[ ]:




