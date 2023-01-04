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
    for a,x in enumerate(nn):
        for b,y in enumerate(nn[a+1:]):
            if x == y: 
                return f"And the birthday is {x}"

print("\n\n")
print(getMatch(nn))




print("""\nThe Birthday Paradox shows us that in a group X of people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)""")
