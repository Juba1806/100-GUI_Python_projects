#!/usr/bin/env python3 


# lmproof is language model proof reader 
import lmproof 

# Enter a text 
text = input("Enter the text: ")

def spellcheck(text):

    # Correct the code using the module 
    proof_reader = lmproof.load("en")    
    corrected = proof_reader.proofread(text)

    # Print the original text 
    print(f"Original: {text}")

    # Print out the correct text 
    print(f"Correction: {corrected}")

spellcheck(text)
    

