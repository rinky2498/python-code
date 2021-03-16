# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:13:47 2021

@author: home
"""
##given string is palindrome or not

sname = input("Given string is: ")

if sname[::-1] == sname[0:]:
  
	print(sname, " is a palindrome")

else:
  
	print(sname, " is not a palindrome")
