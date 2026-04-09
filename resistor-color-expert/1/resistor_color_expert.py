def get_tolerance_value(tolerance_color):
    tolerance_dict = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }
    if not tolerance_color:
        return ""
    return " ±" + str(tolerance_dict[tolerance_color]) + "%"


def get_right_result(raw_result):
    zeros_num = 0
    clean_result = ""

    zeros_num = raw_result % 10
    raw_result = int(raw_result / 10)
    while (raw_result and raw_result % 10 == 0):
        raw_result = int(raw_result / 10)
        zeros_num = zeros_num + 1
    return str(raw_result) + ("0" * int(zeros_num))


def resistor_label(colors):
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
    tolerance_color = ""

    for color in colors:
        raw_result = (raw_result * 10) + colors_dict[color]

    if len(colors) > 1:
        tolerance_color = colors.pop()
        raw_result = int(raw_result / 10)

    clean_result = int(get_right_result(raw_result))
    if 1000 <= clean_result < 1000000:
        ohms_unit = " kiloohms"
        clean_result = clean_result / 1000
    elif 1000000 <= clean_result < 1000000000:
        ohms_unit = " megaohms"
        clean_result = clean_result / 1000000

    if clean_result.is_integer():
        clean_result = int(clean_result)

    return str(clean_result) + ohms_unit + get_tolerance_value(tolerance_color)
