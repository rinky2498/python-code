# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:29:40 2021

@author: home
"""

##program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def Remove(duplicate):
    newlist = []
    for num in duplicate:
        if num not in newlist:
            newlist.append(num)
    return newlist
     
# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))