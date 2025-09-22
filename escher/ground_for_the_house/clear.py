def house(plan):
    plan = plan.strip().split('\n')

    h_rows = [row for row in range(len(plan)) if '#' in plan[row]]

    if not h_rows:
        return 0

    h_cols = []

    for row in range(len(plan)):
        h_cols += [col for col in range(len(plan[0])) if plan[row][col] == '#']

    return (h_rows[-1] - h_rows[0] + 1) * (max(h_cols) - min(h_cols) + 1)
