#!/usr/bin/env python
# coding: utf-8

# Desicion making is most powerful aspect of all programming language. It allows user/developer making desicion.
# The desicion are made on the validity of particular condition.

# In[2]:


age = int(input("Enter your Age: "))
if age > 18:
    print("You are eligible to Vote.")


# Write a python program to check even numbers in python. the numbers are taken from the user.

# In[4]:


number = int(input("Enter Number :"))
if number % 2 == 0:
    print("Entered number is Even.")
else:
    print("Entered number is Odd.")


# Write a python program to take 5 inputs from the user(Name, Age, Qualification, City, Pincode).
# Apply a condition if the user is belongs to Mumbai is eligible for audition, 
# if a user pincode is from mumbai number 9 then user is not eligible for audition 
# also the Qualification of user must be Msc.

# In[10]:


name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
qualification = input("Enter Your Qualification: ").lower()
city = input("Enter Your City: ").lower()
pincode = int(input("Enter Your Pincode: "))

if city == "mumbai":
    print("User is Eligible for Audition")
if pincode == 9:
    print("User is Not Eligible for Audition")
if qualification == "msc":
    print("User is Eligible for Audition")


# In[12]:


age = int(input("Enter your Age: "))
if age >= 18:
    print("Congrats!, You are eligible to Vote.")
else:
    print(f"Oops!, You have to wait for {18 - age} Years.")


# In[1]:


name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
qualification = input("Enter Your Qualification: ").lower()
city = input("Enter Your City: ").lower()
pincode = int(input("Enter Your Pincode: "))

if city == "mumbai":
    print("User is Eligible for Audition")
elif pincode != 9:
    print("User is Eligible for Audition")
elif qualification == "msc":
    print("User is Eligible for Audition")
else:
    print("User is Not Eligible for Audition")


# In[2]:


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




