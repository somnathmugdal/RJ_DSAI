#!/usr/bin/env python
# coding: utf-8

# # Keywords

# Keywords are tghe reserved in python programming language.
# It is used to define syntax of the program.
# It cannot be used as identifier, functions & variable name.
# All keywords in python are written in lower case except True , False & None
# They is case sensitive

# # Operators

# they are used to perform operations on variables.
# 1) Arithmatic operator:
#     + addition x+y
#     - subtrtaction x-y
#     * Multipication x*y
#     / Division x/y
#     % modulus x%y
#     ** Exponentiation x**y
#     // floor division x//y
#     
#  Write a python program to take thre input from useer and perform Addition of first two number and resultant of additon value is multiply by third no of the user.

# In[1]:


a= input("Enter your first number :")
b = input("Enter your second number :")
c = input("Enter your third numberr : ")
d=int(a)+int(b)
print("add is :",d)
e=int(d)*int(c)
print("mul is :",e)


# In[2]:


a= int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
c = int(input("Enter your third number : "))
d=(a)+(b)
print("add is :",d)
e=(d)*(c)
print("mul is :",e)


# Write a python program to take five input from user , first two be float number , and last two be integer value , midle value is name of user 
# 1) divide the last inputs number with first floting point number.
# 2) perform mul of second input number with second last input number
# 3) display name of the user with a prefix "you are not intelligent" 

# In[3]:


a = float(input("Enter your First number :"))
b = float(input("Enter your second number :"))
c = str(input("Enter your name : "))
d = int(input("Enter your third number :"))
e = int(input("Enter your fourth number :"))
f=e/a
print(" divide",f)
g=b*d
print("mul",g)
print(" You are not intelligent",c)


# # Assignment Operators

# In[4]:


x=5
x+=3
print(x)

x=5
x-=3
print(x)

x=5
x*=3
print(x)

x=5
x /= 3
print(x)

x=5
x%=3
print(x)

x=5
x //=3
print(x)

x=3
x **= 3
print(x)

x=5
x&=3
print(x)

x=5
x |=3
print(x)


x^=-3
print(x)

x=3
x >>= 3
print(x)


# # Data types

# In[5]:


e= list["apple","banana","cherry"]
f= tuple(("apple","banana","cherry"))
g= range(6)
h= dict(name = "chetan" , age=23 )
i= set(("apple","banana","cherry"))
j= frozenset(("apple","banana","cherry"))
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)


# In[ ]:




