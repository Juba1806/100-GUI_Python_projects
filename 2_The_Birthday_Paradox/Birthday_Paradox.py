#/usr/bin/env python3

import datetime, random 

def getBirthdays(numberOfBirthdays):
    """ Returns a list of number random date objects for birthdays."""
    birthdays = []

    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all 
        startOfYear = datetime.date(2000,1,1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)

    return birthdays

def getMatch(birthdays):
    """ Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthedays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a , birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[ a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return thematching birthday.
