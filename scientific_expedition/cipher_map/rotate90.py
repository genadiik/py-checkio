def rotate90(matrix):
    size = len(matrix)
    out = []

    for i in range(size):
        out.append([])
        for j in range(size):
            out[i].append(matrix[size-1-j][i])

    return out


def recall_password(cipher_grille, ciphered_password):
    password = ''

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if cipher_grille[j][k] == 'X':
                    password += ciphered_password[j][k]
        cipher_grille = rotate90(cipher_grille)

    return password
