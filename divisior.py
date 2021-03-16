# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:19:47 2021

@author: home
"""
##program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input("enter the no:"))
i = 0

while i < num:
    i = i+1
    
    if num % i == 0:
        print(i)