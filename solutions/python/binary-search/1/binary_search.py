"""
    Binary-Search Algorithm
"""

def find(search_list, value):
    """
        Binary-Search Algorithm
    """
    upper = len(search_list) - 1
    lower = 0
    while lower <= upper:
        middle = lower + ((upper - lower) // 2)
        if value == search_list[middle]:
            return middle
        if value < search_list[middle]:
            upper = middle - 1
        else:
            lower = middle + 1

    raise ValueError("value not in array")
