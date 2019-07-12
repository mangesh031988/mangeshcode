# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:17:13 2019

Python Program to Check Leap Year

@author: Mangesh
"""

year = int(input("enter a year: "))
 
if(year%4==0 and (year%100!=0 or year%400==0)):
	print("leap year")
else:
	print("not leap year")
