#!/usr/bin/env python3
import random 


num_digits = 3 # (!) Try setting this to 1 or 10.
max_guesses = 10 # (!) Try setting this to 1 or 100. 


def main():
    print("""
I am thinking of a {}-sigit number with no repeated digits. 
Try to guess what it is. Here are some clues:
When I say:    That means:
 Pico          One digit is correct but in the wrong position. 
 Fermi         One digit is correct and in the right position. 
 Walo          No digit is correct. 

for example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico. """.format(num_digits))




    while True:
        # This tores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought up  a number.")
        print(f"You have {max_guesses} guesses to get it.")

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ""
            #Keep looping until they enter a valid guess:
            while len(guess) != num_digits or not guess.isdecimal():
                print(f"Guess # {numGuesses}: ")
                guess = input("> ")

                clues = getClues(guess, secretNum)
                if len(clues) < 1:
                    haja = " | ".join(clues)
                    print(haja)
                else:
                    print(clues)
                numGuesses += 1

                if guess == secretNum:
                    print("that is correct")
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

    numbers = list("0123456789")  # Create a list of digits -0 to 9
    random.shuffle(numbers)  # Shuffle them inot random order.

    # Get the first num_digits digits inthe list of the secret number.
    secretNum = ""
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """ Returns a string with pico ,fermi, walo clues for a guess and seecret number pair."""
    if guess == secretNum:
        return "You got it !"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append("F blasto ")

        if guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append("Machi f blasto")
        elif len(clues) == 0:
            return "Walo"  # Thre are no correct digits at all.
        else:
            # Sort the clues into alphabicetical order so their original order
            # doesn't give information away.
            clues.sort()
            # Make a single string for the list of string clues.
            return "".join(clues)


if __name__ == "__main__":
    main()
