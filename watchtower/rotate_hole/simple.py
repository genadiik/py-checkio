def rotate(state, pipe_numbers):
    variants = []
    for i in range(len(state)):
        if all(state[j] == 1 for j in pipe_numbers):
            variants.append(i)
        state.insert(0, state.pop())
    return variants
