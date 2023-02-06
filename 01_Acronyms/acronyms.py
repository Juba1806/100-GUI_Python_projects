#!/usr/bin/env python3

import sys 



# asking the user for input 
text = input("Enter a text\n")

# with  split we put each word in list 
list_text = text.split()

result = ""

for word  in list_text:
    # in each time take the first letter of a word 
    letter = word[0]
    # make each character uppercase
    letter = letter.title()
    # in each time add the letter to the result 
    result += letter


print(len(result))

""" if the result is more than 5 letter that would end up a little ugly, 
so let's deal with it """

if len(result) > 4:
    print("\n\n\nThe acronym is more than 5 letter, are you sure you want it this way?")

    while True:
        answer = input("Press[Y/N]  Y for yes and N for no : ")
        if answer == "Y":
        # if the user said Y we give him the result and exit the program 
           print(result)
           sys.exit() 

        elif answer == "N":
        # if the user select N We want to guide him a little bit 
            print("\n\n\nWe sugest you select the first 5 letters or try to rephrase the sentence!")
            while True:
                answer1 = input("Press[Y/N]  Y for the first 5 letters and N for to exit and rephrase : ")
                if answer1 == "Y":
                    print(result[:5])
                    sys.exit()
                elif answer1 == "N":
                    sys.exit()
                else:
                    print("Please enter Y or N")
                            
        else:
        # if the user try to enter wrong input , We remind him
            print("Please enter Y or N")




print(result)
    
