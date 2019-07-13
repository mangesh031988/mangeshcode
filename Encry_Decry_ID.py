
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:17:51 2019

@author: Mangesh

Case Study 3 :
  Build a system where when user enters Reference ID it is encrypted, 
  so that hackers cannot view the mapping of Reference ID and finger print
  
  1. Read the input from command line – Reference ID
  2. Check for validity – it should be 12 digits and allows on number and alphabet
  3. Encrypt the Reference ID and print it for reference
  4. Allow some special characters in ReferenceID
  5. Give the option for decryption to user

@author: Mangesh
"""

from cryptography.fernet import Fernet
key = Fernet.generate_key() # Store this key or get if you already have it
f = Fernet(key)
val = 1

Generic_id = input("Enter your Generic Id : " )  # To get Generic Id from User

# Validate lneght of Generic Id is greater than 12
if len(Generic_id) < 12:
    print("Generic_ID should be 12 digits and allows on number and alphabet : ")
    val = 0

# Validate Generic Id have at least 1 digit value
if not any(i.isdigit() for i in Generic_id): 
    print('Generic_ID should have at least one numeral') 
    val = 0    

# Validate Generic Id have at least 1 alphabet value
if not any(i.isalpha() for i in Generic_id): 
    print('Generic_ID should have at least one charachter') 
    val = 0  
   
if val == 0:
   print("Generic_ID is Incorrect ")                 
else:
    message = Generic_id.encode()
    encrypted = f.encrypt(message)   # Encryption of Generic_id

    print("Your Encrypted Generic_ID is : ", encrypted)  
    
    decrypted = f.decrypt(encrypted)  # Decryption of Generic_id
    print("Your Decrypted Generic_ID is : ", decrypted)
    
    
