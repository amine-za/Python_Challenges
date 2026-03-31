"""
    Given a name and a number, your task is to produce a sentence using that name and that number as an ordinal numeral. Yaʻqūb expects to use numbers from 1 up to 999.
"""


def get_ordinal_num(number):
    """
        get the ordinal numeral.
    """
    
    number = str(number)

    if len(number) > 1 and (number[-2:] == "11" or number[-2:] == "12" or number[-2:] == "13"):
        return "th"
    if number[-1] == "1" and number[-2:] != "11":
        return "st"
    if number[-1] == "2" and number[-2:] != "12":
        return "nd"
    if number[-1] == "3" and number[-2:] != "13":
        return "rd"
    return "th"


def line_up(name, number):
    """
        Given a name and a number, your task is to produce a sentence using that name and that number as an ordinal numeral. Yaʻqūb expects to use numbers from 1 up to 999.
    """
    
    return name + ", you are the " + str(number) + get_ordinal_num(number) + " customer we serve today. Thank you!"
