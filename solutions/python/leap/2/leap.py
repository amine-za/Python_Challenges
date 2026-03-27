def leap_year(year):
    """
        Your task is to determine whether a given year is a leap year.
    """
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0
