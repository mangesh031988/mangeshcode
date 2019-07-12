# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:22:44 2019

Python Program to Check Prime Number

@author: Mangesh
"""
num = int(input("enter a number: "))
 
for i in range(2, num):
	if num % i  == 0:
		print("not prime number")
		break
else:
	print("prime number")
