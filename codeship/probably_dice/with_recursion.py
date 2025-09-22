def magic(dice_number, sides):
    if dice_number == 1:
        return [1/sides] * sides
    probability_list = [0] * (dice_number*sides+(1-dice_number))
    probability_matrix = []
    prev_list = magic(dice_number-1, sides)
    for i in range(len(prev_list)):
        probability_matrix.append([])
        for j in range(sides):
            probability_matrix[i].append(prev_list[i]*1/sides)
    for p in range(len(probability_list)):
        for i in range(len(probability_matrix)):
            for j in range(sides):
                if i+dice_number-1 + j+1 == p+dice_number:
                    probability_list[p] += probability_matrix[i][j]
    return probability_list


def probability(dice_number, sides, target):
    if target < dice_number or target > dice_number * sides:
        return 0.0
    return round(magic(dice_number, sides)[target-dice_number], 4)
