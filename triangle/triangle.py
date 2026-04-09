"""
    Determine if a triangle is equilateral, isosceles, or scalene.
"""

def is_triangle(sides):
    """
        A function that check if its logic for it to be a triangle depending on the three sides               mesurments
    """
    
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0 or sides[0] + sides[1] < sides[2]:
        return False
    return True


def equilateral(sides):
    """
        An equilateral triangle has all three sides the same length.
    """
    
    sides.sort()
    if not is_triangle(sides):
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    """
        
        An isosceles triangle has at least two sides the same length. (It is sometimes specified as           having exactly two sides the same length, but for the purposes of this exercise we'll say at          least two.)

    """
    
    sides.sort()
    if not is_triangle(sides):
        return False
    if sides[1] == sides[0] or sides[1] == sides[2]:
        return True
    return False
    

def scalene(sides):
    """
        A scalene triangle has all sides of different lengths.
    """

    sides.sort()
    if not is_triangle(sides):
        return False
    if sides[1] != sides[0] and sides[1] != sides[2]:
        return True
    return False
