"""
The Greek mathematician Nicomachus devised a classification scheme for positive integers, identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number not including the number itself. For example, the aliquot sum of 15 is 1 + 3 + 5 = 9.
"""


def get_aliquots(number):
    """ Get all the aliquots of the input integer positive number

    :param number: int a positive integer
    :return: array[int] the aliquots of the input integer number
    """

    aliquots = [1]
    
    for integer in range(2, int((number/2) + 1)):
        if number % integer == 0:
            aliquots.append(integer)
    
    return aliquots


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    number_aliquots = get_aliquots(number)

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if len(number_aliquots) == 1 or sum(number_aliquots) < number:
        return "deficient"
    if sum(number_aliquots) == number:
        return "perfect"
    return "abundant"
