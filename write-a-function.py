# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True  
            else:
                return False 
        else:
            return True 
    else:
        return False  
           
    return leap
