
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:09:10 2019

Write a program, which will find all the numbers between 1000 and 3000 (both included) 
such that each digit of a number is an even number.

@author: Mangesh
"""

numb = int(input("enter a number between 1000 and 3000: "))
 
if(numb%2 == 0):
	print("number is even")
else:
	print("number is odd")
