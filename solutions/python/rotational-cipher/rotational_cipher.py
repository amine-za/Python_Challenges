"""
    The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.
"""


def rotate(text, key):
    """
        The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.
    """
    
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _, character in enumerate(text):
        is_upper = False
        if character.isalpha():
            if character.isupper():
                is_upper = True
                character = character.lower()
            result = result + alphabet[(alphabet.find(character) + key) % 26]
            if is_upper:
                result = result[:-1] + result[-1].upper()
        else:
            result = result + character
    return result
