#!/usr/bin/env python3

# asking the user for input 
text = input("Enter a text\n")

# with  split we put each word in list 
list_text = text.split()

result = ""

for a in list_text:
    # in each time take the first character of a word 
    character = a[0]
    # make each character uppercase
    character = character.title()
    # in each time add the caracter to the result 
    result += character 

print(result)
    
