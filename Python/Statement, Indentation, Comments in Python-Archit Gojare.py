#!/usr/bin/env python
# coding: utf-8

# Keywords 
# 1. Keywords are the reserved word in python programming 
# 2. Used to define syntax of the programme
# 3. Keywords cannot be used as indentifire ,function & Variable
# 4. All the keyword in python are written as lower case excepct True & False & None.
# 5. Keyword are case sensetive

# Operator 
# 1. Operator are used to perfome are used fro variable

# Type of operator
# 1. Arthmethic Operator
# + Addition x+y
# - substaration x-y
# * Multiplication x*y
# / Division x/y
# % Modules x%y
# ~ Exponenctioal x~y

# Write a python programme to perfome addtion of first two number and resultent of addtion value is multiplied by third number 

# In[1]:


a=7
b=9
c=6
d=a+b
e=c*d
print (e)


# In[2]:


# input from taken by user 
a = int(input())
b = int(input())
c = int(input())
d = a+b
e = d*c
print (e)


# Write a python progrmme to take 5 input from the user frist two number should be floating print no and last two no should be lager value than middel input is the name of the user
# 1. divide the last input number with first floating point number 
# 2. Perform multiplication of second input nuumber with second last input number
# 3. Display the name of user with the prefix Yor are not smart

# In[5]:


a = float(input())
b = float(input())
c = str(input())
d = int(input())
e = int(input())

print ("Divistion ",e/a)
print ("Multipication ",b*d)
print (c, " You are smart")


# In[6]:


x=7
x+=4
x


# In[7]:


x=8
x-=4
x


# In[8]:


x=7
x*=4
x


# In[9]:


x=7
x/=4
x


# In[10]:


x=7
x%=4
x


# In[11]:


x=7
x==4
x


# Data Types

# In[17]:


a= ["Archit","Soma","Siddhi"] #List
b= ("Archit","Soma","Siddhi") #tuple
c= range(5)
d=dict(name="Archit",age=22)
e=set(("Archit","Soma","Siddhi"))
f=frozenset(("Archit","Soma","Siddhi"))


# In[16]:


a


# In[18]:


b


# In[19]:


c


# In[20]:


d


# In[21]:


e


# In[22]:


f


# In[ ]:




