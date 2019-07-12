# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 20:49:52 2019

Write a program to check the validity of password given by user. 

Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12

@author: Mangesh
"""

passwd = input("Enter the password to SET : ")
val = 1
SpecialSym =['$', '#', '@'] 
      
if not any(char.islower() for char in passwd): 
    print('Password should have at least one lowercase letter') 
    val = 0

if not any(char.isdigit() for char in passwd): 
    print('Password should have at least one numeral') 
    val = 0    

if not any(char.isupper() for char in passwd): 
    print('Password should have at least one uppercase letter') 
    val = 0
        
if not any(char in SpecialSym for char in passwd): 
    print('Password should have at least one of the symbols $@#') 
    val = 0

if len(passwd) < 6: 
    print('length should be at least 6') 
    val = 0
          
if len(passwd) > 20: 
    print('length should be not be greater than 8') 
    val = 0
 
if val == 0:
   print("Your password is Incorrect ")                 
else:
    print("You have sucessfully set password")
    print("Your Password is : " +passwd)
