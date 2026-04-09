"""
            Introduction
        There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chessboard, with the number of grains doubling on each successive square.
        
        Instructions
        Calculate the number of grains of wheat on a chessboard.
        
        A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
        
        Write code that calculates:
        
        the number of grains on a given square
        the total number of grains on the chessboard
"""

def square(number):
    """
            the number of grains on a given square
    """
    
    grains_in_square = 1
    
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    for _ in range(number-1):
        grains_in_square = grains_in_square * 2

    return grains_in_square


def total():
    """
        the total number of grains on the chessboard
    """
    
    grains_in_square = 1
    total_grains = 1

    for _ in range(63):
        grains_in_square = grains_in_square * 2
        total_grains = total_grains + grains_in_square
    
    return total_grains
