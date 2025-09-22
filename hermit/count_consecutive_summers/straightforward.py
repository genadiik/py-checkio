def count_consecutive_summers(num):
    count = 1
    for i in range(1, int(num/2+1)):
        result = j = i
        while result < num:
            j += 1
            result += j
        if result == num:
            count += 1
    return count
