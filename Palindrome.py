

"""
Created on Mon Jul  8 00:22:44 2019

Question 5.Design a code which will find the given number is Palindrome number or not.

@author: Mangesh
"""

abc = int(input("enter a number: "))
 
xyz = abc
rev = 0
 
while xyz != 0:
	rev = (rev * 10) + (xyz % 10)
	xyz = xyz // 10
 
if abc == rev:
	print("number is palindrome")
else:
	print("number is not palindrome")
