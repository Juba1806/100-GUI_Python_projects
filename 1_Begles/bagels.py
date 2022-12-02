#!/usr/bin/env python3

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10 # (!) Try setting this to 1 or 100. 


def main():
    print(""" 
I am thinking of a {}-sigit number with no repeated digits. 
Try to guess what it is. Here are some clues:
When I say:    That means:
 Pico          One digit is correct but in the wrong position. 
 Fermi         One digit is correct and in the right position. 
 Walo          No digit is correct. 

for example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico. """.format(NUM_DIGITS))
