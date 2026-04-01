"""
    The goal of this exercise is to create a way:

to look up the numerical value associated with a particular color band
to list the different band colors
"""


def color_code(color):
    """
        The goal of this exercise is to create a way:
    
    to look up the numerical value associated with a particular color band
    to list the different band colors
    """

    colors_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return colors_dict[color]


def colors():
    """
        The goal of this exercise is to create a way:

to look up the numerical value associated with a particular color band
to list the different band colors
    """
    
    colors_dict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
    return list(colors_dict.keys())