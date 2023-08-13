#!/usr/bin/env python
# coding: utf-8

# Python if-else Statement 

# Decision making a most powerful programme aspect of all programming languages, it allows user/ programmer making decision, the decision are made on validity of particula condiotion 

# In[4]:


age=int(input("Enter Your age "))
if age>18:
    print("You are eligiable to Vote")


# In[23]:


#Write a python programme to check even number in python, the number is taken from user

Number=int(input("Enter a Number "))
if Number%2==0:
    print(Number,"is even number")


# In[39]:


# Write a python programme to take 5 input form user (name,age,qulification,city,pincode)
# Appply a condtion if user belong to mumbai he is eligiable from audition 
# if a user pincode is Mumbai number 9 then user is not eligiable for audition also the qualification of user must be MSC

name=str(input("Enter a name: "))
age=int(input("Enter a age: "))
qulification=str(input("Enter a qulification: "))
city=str(input("Enter a city: "))
pin=int(input("Enter a pin: "))


if pin==9:
    print("You are not eligiable")
elif city=="Mumbai":
    print("You are eligiable")
elif qulification=="Msc":
    print("You are eligiable")


# In[35]:


age=int(input("Enter a age: "))
if age>=18:
    print("You are eligiable for vote")
else:
    print ("Wait for",18-age,"Year")


# In[6]:


num=int(input("Enter a Number: "))
if num<0:
    print("Number is Negetive")
elif num==0:
    print("Number is 0")    
elif num<20:
    print("Number is between 01 to 19")
elif num<50:
    print("Number is between 20 to 49")
elif num<100:    
    print("Number is between 50 to 99")
else:
    print("Enter number between 1 to 99")


# In[ ]:




