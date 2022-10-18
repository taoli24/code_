roman_int_map = {
    'iv': 4,
    'ix': 9,
    'xl': 40,
    'xc': 90,
    'cd': 400,
    'cm': 900,
    'i': 1,
    'v': 5,
    'x': 10,
    'l': 50,
    'c': 100,
    'd': 500,
    'm': 1000
}


def romanToInt(s):
    s = s.lower()
    roman_numbers = []
    i = 0
    if len(s) == 1:
        return roman_int_map[s]

    while i < len(s) - 1:
        if (s[i] == 'i' and (s[i + 1] == 'v' or s[i + 1] == 'x')) or \
                (s[i] == 'x' and (s[i + 1] == 'l' or s[i + 1] == 'c')) or \
                (s[i] == 'c' and (s[i + 1] == 'd' or s[i + 1] == 'm')):
            roman_numbers.append(s[i:i + 2])
            i += 1
        else:
            roman_numbers.append(s[i])
        i += 1
        if i == len(s)-1:
            roman_numbers.append(s[i])
    return sum(roman_int_map[key] for key in roman_numbers)


print(romanToInt("v"))
