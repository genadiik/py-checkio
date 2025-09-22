import time as t


def time_converter(time):
    return t.strftime('%H:%M', t.strptime(time.replace('.', ''), '%I:%M %p'))
