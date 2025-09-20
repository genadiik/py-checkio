def checkio(first, second):
    words = f'{first},{second}'.split(',')
    return ','.join(sorted([w for w in set(words) if words.count(w) > 1]))
