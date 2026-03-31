"""
    Your task is to figure out if a sentence is a pangram.
    A pangram is a sentence using every letter of the alphabet at least once.
"""


def is_pangram(sentence):
    """
        Your task is to figure out if a sentence is a pangram.
        A pangram is a sentence using every letter of the alphabet at least once.
    """
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    return all(
        char in sentence
        for char in alphabets
    )
