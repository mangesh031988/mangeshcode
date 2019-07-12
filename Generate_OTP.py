# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:17:13 2019

Python Program to Generate OTP code

@author: Mangesh
"""

import math, random 
string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
OTP = ""
length = len(string) 
for i in range(9): 
    OTP += string[math.floor(random.random() * length)] 
print("OTP : " +OTP)
  
