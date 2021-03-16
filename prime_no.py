# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 14:11:21 2021

@author: home
"""

##Ask the user for a number and determine whether the number is prime or not.

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")   
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  