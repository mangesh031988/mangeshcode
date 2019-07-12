
    
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 00:08:26 2019

Write a code which accepts a sequence of words as input and 
prints the words in a sequence after sorting them alphabetically.

@author: Mangesh
"""

print("Enter strings:")
x = input()

words = x.split()  
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word)  

