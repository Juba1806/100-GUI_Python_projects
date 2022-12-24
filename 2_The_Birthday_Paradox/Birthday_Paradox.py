#!/usr/bin/env python3


import datetime, random 
from cowsay import cow as simo

def getBirthdays(number):
    """ Returns a list of random birthdays """
    
    birthdays = []

    # The start of the year and the year is unimportant for our simulation
    startday = datetime.date(2000, 1, 1)

    for i in range(number):
    # Generate ramdom birthdays from the year 
        

        #random day from the year 
        randomday = datetime.timedelta(random.randint(0,365))

        Birthday = startday + randomday
        birthdays.append(Birthday)

    return birthdays

nn = getBirthdays(25)

print(nn)








def haja(nn):

    if len(nn) == len(set(nn)):
        return simo(" iwa nn")

    elif len(nn) != len(set(nn)):
         return simo(" Ahh a sat kayn")


print("\n\n\n\n")
print(haja(nn))
