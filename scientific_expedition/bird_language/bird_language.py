VOWELS = "aeiouy"


def translation(phrase):
    result = ''
    i = 0
    while i < len(phrase):
        result += phrase[i]
        if phrase[i] == ' ':
            i += 1
        elif phrase[i] in VOWELS:
            i += 3
        else:
            i += 2
    return result
