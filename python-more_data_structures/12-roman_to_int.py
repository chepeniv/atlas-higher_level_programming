#!/usr/bin/python3
def roman_to_int(roman):
    calc = 0
    ref = {
        'Null': 0,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if type(roman) is not str:
        return 0

    for i in range(len(roman)):
        a = roman[i]
        try:
            b = roman[i + 1]
        except (IndexError):
            b = 'Null'

        m = ref.get(a)
        n = ref.get(b)
        if m >= n:
            calc += m
        else:
            calc -= m

    return calc
