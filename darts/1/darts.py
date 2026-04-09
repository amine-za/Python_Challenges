"""
    Instructions
    Calculate the points scored in a single toss of a Darts game.
"""

import math

def score(x, y):
    """
        Instructions
        Calculate the points scored in a single toss of a Darts game.
    """
    radius = math.ceil((math.hypot(abs(x), abs(y))))

    if -1 <= radius <= 1:
        return 10
    if -5 <= radius <= 5:
        return 5
    if -10 <= radius <= 10:
        return 1
        
    return 0
