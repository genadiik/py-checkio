def to_camel_case(name):
    return ''.join(map(lambda w: w.capitalize(), name.split('_')))
