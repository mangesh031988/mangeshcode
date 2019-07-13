# -*- coding: utf-8 -*-
"""
Created on Mon Jul  12 00:17:13 2019

@author: Mangesh
"""

str = int(input("Enter the number to find the Sum of the Series : "))
agg = 0

if str <= 0:
    print("Kindly enter value greater than 0")
elif str > 0:
  for i in range(1,str+1):
            agg = agg+(1/i)
            
print("Sum of series for input number is : ", round(agg,2))   
