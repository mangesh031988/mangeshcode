# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:07:06 2019

Calculate Factorial for the input number

@author: Mangesh
"""

## Factorial 5!=5*4*3*2*1 = 120

#Declare
number = 9

#Factorial
factorial = 1

if number < 0:
    print("Factorial does not exists for -Ve numbers")
elif number == 0:
    print("The Factorial for 0 is 1")
else:
    for i in range(1,number + 1):
        factorial = factorial*i
    print("The Factorial for", number, "is",factorial )
