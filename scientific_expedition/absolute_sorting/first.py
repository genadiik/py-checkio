def numbers_insert(numbers: list, number: int) -> list:
    if len(numbers) == 0:
        return [number]
    numbers_new = numbers[:]
    for i in range(len(numbers)):
        if abs(numbers[i]) > abs(number):
            numbers_new.insert(i, number)
            return numbers_new
    numbers_new.append(number)
    return numbers_new

def checkio(numbers_array: tuple) -> list:
    numbers = []
    for n in numbers_array:
        numbers = numbers_insert(numbers, n)
    return numbers

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
