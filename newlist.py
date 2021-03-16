# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:23:32 2021

@author: home
"""

##Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

thislist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newlist= [item for item in thislist if item % 2 == 0]
print(newlist)

