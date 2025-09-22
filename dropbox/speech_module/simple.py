FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]


def checkio(number):
    result = ''
    if number >= 100:
        result += f'{FIRST_TEN[int(number/100)]} hundred '
        number %= 100
    if number >= 20:
        result += f'{OTHER_TENS[int(number/10)-2]} {FIRST_TEN[number % 10]}'
    elif number >= 10:
        result += SECOND_TEN[number % 10]
    else:
        result += FIRST_TEN[number]
    return result.rstrip()
