
def isLeapYear(Year):
    # Conditional test for a year that is a leap year
    if ((Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0):
        return 1
    
    # Conditional test for a year that is not a leap year
    if (Year % 4 != 0 or (Year % 100 == 0 and Year % 400 != 0)):
        return 0