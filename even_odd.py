# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:40:33 2021

@author: home
"""

##2. Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

number = input("Enter a number > ")
if int(number) % 2 == 0:
    print(str(number) + " is an Even number.")
else:
    print(str(number) + " is an Odd number.")