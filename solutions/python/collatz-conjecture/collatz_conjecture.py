"""
One evening, you stumbled upon an old notebook filled with cryptic scribbles, as though someone had been obsessively chasing an idea. On one page, a single question stood out: Can every number find its way to 1? It was tied to something called the Collatz Conjecture, a puzzle that has baffled thinkers for decades.

The rules were deceptively simple. Pick any positive integer.

If it's even, divide it by 2.
If it's odd, multiply it by 3 and add 1.
Then, repeat these steps with the result, continuing indefinitely.
example: 12 ➜ 6 ➜ 3 ➜ 10 ➜ 5 ➜ 16 ➜ 8 ➜ 4 ➜ 2 ➜ 1
"""

def steps(number):
    """
        Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
    """
    steps_number = 0
    
    if (number % 2 == 1 and number != 1) or number == 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        elif number % 2 == 1:
            number = (number * 3) + 1
        steps_number = steps_number + 1

    return steps_number