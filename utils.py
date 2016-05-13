def dec_to_bin(s, size):
    s = int(s)
    res = ''
    while s:
        res = str(s % 2) + res
        s //= 2
    res = '0' * (size - len(res)) + res
    return res


def bin_to_dec(s):
    return sum(2 ** (7 - index) * int(bit) for index, bit in enumerate(s))


def chunks(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]
