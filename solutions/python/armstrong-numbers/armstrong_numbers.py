"""
    A Module
"""

def is_armstrong_number(number):
    """
        is_armstrong_number function:
        An Armstrong number is a number that is the sum of its own digits each raised to the power of           the number of digits.
    """
    number_str = str(number)
    number_len = len(number_str)

    total = sum(int(char) ** number_len for char in number_str)

    return number == total