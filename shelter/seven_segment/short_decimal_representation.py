def seven_segment(lit_seg, broken_seg):
    digits = (126, 48, 109, 121, 51, 91, 95, 112, 127, 123)
    count = 1

    for pos in ('ABCDEFG', 'abcdefg'):
        lit = int(''.join(['1' if c in lit_seg else '0' for c in pos]), 2)
        broken = int(''.join(['1' if c in broken_seg else '0' for c in pos]), 2)
        count *= len([dig for dig in digits if dig - (dig & broken) == lit])

    return count
