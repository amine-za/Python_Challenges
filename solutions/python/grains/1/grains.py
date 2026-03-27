def square(number):
    i = 1
    grains_num = 1
    
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    while i in range(number):
        grains_num = grains_num *2
        i = i + 1

    return grains_num


def total():
    i = 1
    grains_num = 1
    grains_total = 1

    while i < 64:
        grains_num = grains_num * 2
        grains_total = grains_total + grains_num
        i = i + 1
    
    return grains_total
