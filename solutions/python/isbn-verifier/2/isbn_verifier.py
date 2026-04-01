"""
    Given a string the program should check if the provided string is a valid ISBN-10. 
"""


def number_check(clean_isbn):
    """
        Check if the isbn input is just numbers except for the last character
    """

    return all(
        row.isdigit()
        for index, row in enumerate(clean_isbn)
    )


def is_valid(isbn):
    """
        Given a string the program should check if the provided string is a valid ISBN-10. 
    """

    result = 0
    
    # Parsing
    if not isbn or ((len(isbn) != 13 and isbn.count("-") != 3) and len(isbn) != 10):
        return False
    
    # Removing the Dashes from the isbn string
    clean_isbn = isbn.replace("-", "")

    # Parsing
    if (clean_isbn[-1].isalpha() and clean_isbn[-1] != "X") or not number_check(clean_isbn[:-1]):
        return False

    # Core concept
    for index, row in enumerate(clean_isbn):
        if row.isalpha():
            break
        result = result + (int(row) * (10 - index))
    if clean_isbn[-1] == "X":
        result = result + 10
    result = result % 11

    return result == 0 and (not clean_isbn[-1].isalpha() or clean_isbn[-1] == "X")
