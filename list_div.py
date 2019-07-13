
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  12 00:17:13 2019

Question 11. By using list comprehension, please write a program to print the list 
             after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
str = [12,24,35,70,88,120,155]    

@author: Mangesh
"""

str = [12,24,35,70,88,120,155]  
  
# Identifying number divisible by 5 and 7
for i in sorted(str):  
    if (i%5==0 and i%7==0):
        str.remove(i)
           
# printing modified list 
print (*str) 
