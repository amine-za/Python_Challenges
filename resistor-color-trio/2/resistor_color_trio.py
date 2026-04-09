"""
    In Resistor Color Duo you decoded the first two colors. For instance: orange-orange got the main value 33. The third color stands for how many zeros need to be added to the main value. The main value plus the zeros gives us a value in ohms. For the exercise it doesn't matter what ohms really are. For example:

orange-orange-black would be 33 and no zeros, which becomes 33 ohms.
orange-orange-red would be 33 and 2 zeros, which becomes 3300 ohms.
orange-orange-orange would be 33 and 3 zeros, which becomes 33000 ohms.
"""


def get_right_result(raw_result: int):
    """
        A function that count how many zeros there are, and clean the raw_result from them
    """

    zeros_num = 0

    zeros_num = raw_result % 10
    raw_result = int(raw_result / 10)
    while (raw_result and raw_result % 10 == 0):
        raw_result = int(raw_result / 10)
        zeros_num = zeros_num + 1
    return raw_result, zeros_num


def label(colors):
    """
        Core logic
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
    raw_result = 0
    ohms_unit = " ohms"

    for color in colors[:3]:
        raw_result = (raw_result * 10) + colors_dict[color]
    # 6543
    raw_result, zeros_num = get_right_result(raw_result)
    if zeros_num <= 2:
        ohms_unit = " ohms"
    elif 2 < zeros_num < 6:
        ohms_unit = " kiloohms"
        zeros_num = zeros_num - 3
    elif zeros_num < 9:
        ohms_unit = " megaohms"
        zeros_num = zeros_num - 6
    else:
        ohms_unit = " gigaohms"
        zeros_num = zeros_num - 9
    return str(raw_result) + ("0" * zeros_num) + ohms_unit
