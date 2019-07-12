
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:17:13 2019

Write a program that accepts a sentence and calculate the number of letters and digits.

@author: Mangesh
"""

string=input("Enter string combination letter and digit:")
cnt1=0
cnt2=0
for i in string:
      if(i.isdigit()):
            cnt1=cnt1+1
      elif(i.isalpha()):      
            cnt2=cnt2+1
print("The number of digits is:")
print(cnt1)
print("The number of letters is:")
print(cnt2)


