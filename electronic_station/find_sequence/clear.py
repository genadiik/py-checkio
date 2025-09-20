SEQ_LENGTH = 4


def find_sequence(row: list) -> bool:
    for i in range(len(row)-SEQ_LENGTH+1):
        if len(set(row[i:i+SEQ_LENGTH])) == 1:
            return True
    return False


def checkio(matrix):
    rows = matrix[:]
    size = len(matrix)
    diags_u = [[] for n in range(2*size-1)]
    diags_d = [[] for n in range(2*size-1)]

    for i in range(size):
        rows.append([row[i] for row in matrix])
        for j in range(size):
            diags_u[i+j].append(matrix[i][j])
            diags_d[j-i+size-1].append(matrix[i][j])

    diags = [diag for diag in diags_u+diags_d if len(diag) >= SEQ_LENGTH]

    return any(map(find_sequence, rows+diags))
