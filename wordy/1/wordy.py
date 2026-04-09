import operator

def replace_by(question):
    """
        Add an underscore between multiplied/divided and the "by"
        Why?: In the main function, i used the split() function to separate the input into arguments, but i faced a problem with the "by". 
    """
    question = question.replace("multiplied by", "multiplied_by")
    question = question.replace("divided by", "divided_by")
    return question


def syntax_check(words_set, math_ops):
    """
        The Ultimate (I think :)) parsing function
        Error Examples:
        by What is by 3 by by plus 2? 
        what is 3 plus 2 multiplied by 3!
        What is 3 plus 2 multiplied 
        What by is 3 by plus by 2 multiplied by 5?
    """
    if not words_set or words_set[:2] != ["What", "is"] or words_set[-1][-1] != "?" \
            or len(words_set) < 3:
        raise ValueError("syntax error")
        
    number_pointer = 2
    words_set[-1] = words_set[-1][:-1]    # Remove the "?" character from the last number
        
    for index in range(len(words_set) - 1, 1, -1):  # start from end
        if (index % 2 == 0 and not words_set[index].lstrip("-").isdigit()):
            raise ValueError("syntax error")
        if (index % 2 == 1 and  words_set[index].lstrip("-").isdigit()):
            raise ValueError("syntax error")
    
    if not words_set[-1].lstrip("-").isdigit():
        if words_set[-1] in math_ops:
            raise ValueError("syntax error")
        raise ValueError("unknown operation")
        
    return words_set


def answer(question):
    """
        The core function
    """
    # "What is 5 multiplied by 13?"  --> ["What", "is", "5", "multiplied_by", "13"]
    words_set = replace_by(question).split() 
    
    operation = "" # Stores the operations "+ - * /" when looping on the input
    math_ops = ["plus", "minus", "multiplied_by", "divided_by"]
    ops = {
        "plus": operator.add,
        "minus": operator.sub,
        "multiplied_by": operator.mul,
        "divided_by": operator.truediv
        }
    words_set = syntax_check(words_set, math_ops)
    result = int(words_set[2])
    
    for index in range(2, len(words_set) - 2, 2):
        second_num = int(words_set[index + 2])
        operation = words_set[index + 1]
        if not operation in math_ops:
            raise ValueError("unknown operation")
        result = ops[operation](result, second_num)
    
    return result
