# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:07:06 2019
Python Program to Check Armstrong Number
@author: Mangesh
"""

num = int(input("enter a number: "))
 
lgth = len(str(num))
agg = 0
var = num
 
while(var != 0):
	agg = agg + ((var % 10) ** lgth)
	var = var // 10
 
if agg == num:
	print("armstrong number")
else:
	print("not armstrong number")
  
