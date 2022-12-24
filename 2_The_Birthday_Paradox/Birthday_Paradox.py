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

        Birthday = startday + randomday
        birthdays.append(Birthday)

    return birthdays

nn = getBirthdays(25)

print(nn)





