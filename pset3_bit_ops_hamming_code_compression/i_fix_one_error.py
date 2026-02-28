def encode(s):
    s = list(map(int, s))
    n = len(s)

    res = [0]
    control_bit = 1
    i = 1
    j = 0
    while j < n:
        if i == control_bit:
            res.append(0)
            control_bit <<= 1
        else:
            res.append(s[j])
            j += 1
        i += 1
    # print(res)

    n = len(res)
    control_bit = 1
    while control_bit < n:
        res[control_bit] = 1
        for i in range(control_bit + 1, n):
            if i & control_bit:
                res[control_bit] ^= res[i]
        control_bit <<= 1
    # print(res)

    return "".join(map(str, res[1:]))


def fix_and_decode(s):
    s = [0] + list(map(int, s))
    n = len(s)

    control_bit = 1
    corrupted_bit = 0
    while control_bit < n:
        for i in range(control_bit + 1, n):
            if i & control_bit:
                s[control_bit] ^= s[i]
        if not s[control_bit]:
            corrupted_bit |= control_bit
        control_bit <<= 1
    s[corrupted_bit] ^= 1

    # print(corrupted_bit - 1)
    res = []
    control_bit = 1
    i = 1
    while i < n:
        if i == control_bit:
            control_bit <<= 1
        else:
            res.append(s[i])
        i += 1

    return "".join(map(str, res))


def main():
    op = input()
    if op == "1":
        print(encode(input()))
    else:
        print(fix_and_decode(input()))


if __name__ == "__main__":
    main()
