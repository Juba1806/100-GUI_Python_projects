#!/usr/bin/env python3

print("\nBagels, a deductive logic game.") 
print("\n\n\n")

print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:\n")

print("When I say:    That means:")
print("\n Pico\t\tOne digit is correct but in the wrong position.")
print(" Fermi\t\tOne digit is correct and in the right position.")
print(" Bagels\t\tNo digit is correct.")

print("\nI have thought up a number.")
print(" You have 10 guesses to get it.")


x = 1 
y = 3 
z = 8 

for a in range(1,10):
    number = input(f"Guess #{a}  ")
    number = x + y + z 

    if number == x or number == y or number == z:
        print("Pico")
    elif number== x and number == y or number == y and number == z or number == z and x:
        print("Pico Pico")
    elif number == x and number == y and  number == z : 
        print("you got this")
    else:
        print("no you wrong")
