#!/usr/bin/python3
def best_score(a_dictionary, default=None):
    if not a_dictionary:
        return default
    return max(a_dictionary, key=a_dictionary.get)
