"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    if isinstance(record, tuple) and len(record) == 2:
        return record[1]
    raise ValueError("Value error")


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    if isinstance(coordinate, str) and coordinate:
        return tuple(coordinate)
    raise ValueError("Value error")
    

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    if isinstance(azara_record, tuple) and len(azara_record) == 2 and \
            isinstance(rui_record, tuple) and len(rui_record) == 3 and \
            tuple(azara_record[1]) == tuple(rui_record[1]):
        return True
    return False
    # raise ValueError("Value error")


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    if compare_records(azara_record, rui_record):
        return tuple((azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2]))
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """

    result = ""
    for record in combined_record_group:
        if tuple(record[1]) == tuple(record[3]):
            result += str(record[:1] + record[2:])

    result = result.replace(")(", ")\n(") + "\n"
    return (result)

"('Sc[854 chars], 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')"
"('Sc[854 chars], 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')\n"
