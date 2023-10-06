#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = 0
    new = None
    for key, value in a_dictionary.items():
        if value > highest:
            new = key
            highest = value
    return new
