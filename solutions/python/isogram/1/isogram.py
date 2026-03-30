"""
    Determine if a word or phrase is an isogram.
"""

def is_isogram(string):
    """
        Determine if a word or phrase is an isogram.
    """
    # enumerate
    string = string.lower()
    for character in string:
       if character.isalpha() and string.count(character) > 1:
            return False
    return True
