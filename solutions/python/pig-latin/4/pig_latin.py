"""
    Instructions
Your task is to translate text from English to Pig Latin. The translation is defined using four rules, which look at the pattern of vowels and consonants at the beginning of a word. These rules look at each word's use of vowels and consonants
"""


def is_vowel(character):
    """
        check if the passed character as an input is a vowel character
    """

    if not character or not character.isalpha() or len(character) > 1:
        raise ValueError("bad input")
    
    return character.lower() in "aeiou"


def move_consonants_to_end(text):
    """
        Rule 2 function: move the consonants to the end
    """

    while not is_vowel(text[0]):
        text = text + text[0]
        text = text[1:]
    text = text + "ay"
    return text


def move_consonant_cluster_with_qu(text):
    """
        Rule 3 function: move 'qu' and consonants to the end
    """

    while True:
        if text[0] == "q" and text[1] == "u":
            text = text + "quay"
            text = text[2:]
            break
        text = text + text[0]
        text = text[1:]
    return text


def check_part_after_consonants(text, expression, length):
    """
        Checks if the expression do appear in the text before any vowel
    """

    for index, row in enumerate(text): 
        if is_vowel(row): 
            break
        if text[index : index + length] == expression: 
            return True 
    return False


def move_consonants_before_y(text):
    """
        Rule 4 function: move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.
    """

    while text[0] != "y":
        text = text + text[0]
        text = text[1:]
    text = text + "ay"
    return text


def translate(text):
    """
        The main programs function
    """
     
    result_answer = ""
    result_word = ""

    if not text:
        raise ValueError("bad input")
    text_arr = text.split()
    for index, word in enumerate(text_arr):
        if not word or not word.strip():
            raise ValueError("bad input")
        if is_vowel(word[0]) or word[:2] == "xr" or word[:2] == "yt":
            result_word = word + "ay"
        elif not is_vowel(word[0]):
            if check_part_after_consonants(word, "qu", 2):
                result_word = move_consonant_cluster_with_qu(word)
            elif word[0] != "y" and check_part_after_consonants(word, "y", 1):
                result_word = move_consonants_before_y(word)
            else:
                result_word = move_consonants_to_end(word)
        result_answer = result_answer + result_word
        if index < len(text_arr) - 1:
            result_answer = result_answer + " "
    return result_answer
    