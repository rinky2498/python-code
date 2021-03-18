# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:50:31 2021

@author: home
"""

from datetime import datetime

p_name = input("enter the name of person:")
p_age = int(input("enter the age of person:"))
if p_age>=100:
  print("your age is more than hundred") 
else:
   h_year= (100-p_age)+datetime.now().year
    
   print("In year",h_year,"you will turn 100 years old.")
