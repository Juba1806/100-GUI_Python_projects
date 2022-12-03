#!/usr/bin/env python3

num_digits = 3 # (!) Try setting this to 1 or 10.
max_guesses = 10 # (!) Try setting this to 1 or 100. 


def main():
    print(f""" 
I am thinking of a {num_digits}-sigit number with no repeated digits. 
Try to guess what it is. Here are some clues:
When I say:    That means:
 Pico          One digit is correct but in the wrong position. 
 Fermi         One digit is correct and in the right position. 
 Walo          No digit is correct. 

for example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico. """)

 
while True:
    # This tores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print("I have thought up  a number.")
    print(f"You have {max_guesses} guesses to get it.")

    numGuesses = 1 
    while numeGuesses <= max:
        guess = "" 
        #Keep looping until they enter a valid guess:
        while len(guess) != num_digits or not guess.isdecimal():
            print("GUess # {}: ".format(numGuesses))
            guess = input("> ")

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses +=1 

        if guess == secretNum:
            break # They're correct, so break out of this loop. 
        if numGuesses > max_guesses:
            print("you ran out of guesses.")
            print(f"The answer was {secretNum}.")

        # Ask player if they want to play again.
        print(" Do you want to play again.")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing ! ")






def getSecretNum():
    """ Returns a string made up of num_ditis unique random digits."""

    numbers = list("0123456789")    # Create a list of digits -0 to 9 
    random.shuffle(numbers) # Shuffle them inot random order.

    # Get the first num_digits digits inthe list of the secret number.
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

