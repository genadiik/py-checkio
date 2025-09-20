import re

def from_camel_case(name):
    return re.sub(r'([A-Z])', r'_\1', name)[1:].lower()
