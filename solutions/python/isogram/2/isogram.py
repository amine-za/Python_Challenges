"""
    Determine if a word or phrase is an isogram.
"""


def is_isogram(string):
    """
        Determine if a word or phrase is an isogram.
    """

    string = string.lower()
    return not any(
        char.isalpha() and string.count(char) > 1
        for char in string
    )
