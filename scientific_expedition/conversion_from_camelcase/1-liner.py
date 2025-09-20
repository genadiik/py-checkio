def from_camel_case(name):
    return ''.join([f'_{c}' if c.isupper() else c for c in name])[1:].lower()
