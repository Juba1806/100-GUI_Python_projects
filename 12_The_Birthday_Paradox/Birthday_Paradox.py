#!/usr/bin/env python3


import datetime, random 

def getBirthdays(number):
    """ Returns a list of random birthdays """
    
    birthdays = []

    # The start of the year and the year is unimportant for our simulation
    startday = datetime.date(2000, 1, 1)

    for i in range(number):
    # Generate ramdom birthdays from the year 
        

        #random day from the year 
        randomday = datetime.timedelta(random.randint(0,365))
        Birthday = randomday + startday 

        birthdays.append(Birthday)

    return birthdays

nn = getBirthdays(25)

print(nn)



def getMatch(nn):
    """"Returns the date object of a birthday that occurs more than once in the birthdays list."""

    if len(nn) == len(set(nn)):
        return "There's no matching birthday"
    

    # Compare each birthday
    for a, x in enumerate(nn):
        for b, y in enumerate(nn[a+1:]):
            if  x == y: 
                return f"And the birthday is {x}"

print("\n\n")




print("""\nThe Birthday Paradox shows us that in a group X of people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)""")





# set up a tuple of month names in order 
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
	'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


while True:
    # Kepp asking until the user enters a valid a mount . 
    print("How many birthdays shall I generate ? (Max 100)")
    response = input("> ")
    if response.isdecimal() and 0 < int(response) < 100:
       numBdays = int(response) 
       break # User has enter a valid amoutn . 
print()







# Generate and display the birthdays : 
print("here are", numBdays, "birthdays:")
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # DEsply a come for each birthday after the first birthday.
        print(', ',end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = f"{monthName} {birthday.day}"
        print(dateText , end="")
print()
print()



# Determine if there are two birthdays that match.
match = getMatch(birthdays)


# Dispay the results: 
print("In this simulation, ",end="")

if match != None:
    monthName = MONTHS[match.month -1 ]
    dateText = f"{monthName} {match.day}"
    print(f" multiple people have a birthday on {dateText}")
else:
    print("there are no matching birthdays.")
print()

# Run through 100,100 simulations:
print("Generating", numBDays , "random birthdays 100,00 times...")
input("Press Enter to begin... ")

print("Let's run another 100,000 simulations.")
simMatch = 0 # HOw many simulation had matching birthdays in them 

for i in range(100_000):
    # Report on the progress every 10,100 simulations:
    if i % 10_000 == 0:
        print(i, "simulations run...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1 
print("100_000 simulations run.")


# Display simulation results:

probability = round(simMatch / 100_000 * 100 , 2)

print("Out of 100,000 simulations of", numBdays ,"people , there was a ")
print("matching birthday in that group" , simMatch, "times. This means")
print("that", numBdays, "people have a"< probability, "%chance of")
print("having a maching birthday in their group.")
print("That\"s probably more than you would think ! ")


