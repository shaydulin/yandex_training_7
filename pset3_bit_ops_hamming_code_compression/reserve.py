from string import ascii_lowercase


BITS = 8
TOTAL = 2**BITS
N = BITS - 26
idxs_of_letters = {
    ch: i for ch, i in zip(ascii_lowercase, range(N, TOTAL))
}
letters_by_idcs = {
    i: ch for ch, i in zip(ascii_lowercase, range(N, TOTAL))
}
TRIE = {}
TRIE[0] = 0
WORDS = [""]


def convert_idx(i):
    res = []
    while i:
        i, r = divmod(i, N)
        res.append(r)
    res.reverse()
    return res


def pack(s):
    cur = TRIE
    res = []
    for ch in s:
        if ch in cur:
            cur = cur[ch]
        else:
            res.extend(convert_idx(cur[0]))
            res.append(idxs_of_letters[ch])
            cur[ch] = {}
            cur[ch][0] = len(WORDS)
            WORDS.append(WORDS[cur[0]] + ch if 0 in cur else ch)
            cur = TRIE
    if not cur is TRIE:
        res.extend(convert_idx(cur[0]))
    print(f"Compression rate: {len(res) / len(s)}")
    print(f"Dict len: {len(WORDS)}")
    print(f"Letters left: {sum(chunk for chunk in res if chunk >= N)}")
    return res


def unpack(s: str):
    res = []
    prev_word_idx = 0
    for chunk in map(int, s.split()):
        if chunk >= N:
            WORDS.append(WORDS[prev_word_idx] + letters_by_idcs[chunk])
            prev_word_idx = 0
            res.append(WORDS[-1])
        else:
            prev_word_idx = prev_word_idx * N + chunk
    if prev_word_idx:
        res.append(WORDS[prev_word_idx])
    return "".join(res)


def main():
    op = input()
    if op == "pack":
        print(*pack(input()))
    else:
        print(unpack(input()))


def test():
    with open("j_tests.txt") as file:
        for _ in range(6):
            s = file.readline().strip()
            res = " ".join(map(str, pack(s)))
            s_ = unpack(res)
            print("Strings match" if s == s_ else "Strings do not match")
            print("=" * 20)


if __name__ == "__main__":
    # main()
    test()


#############################################


from string import ascii_lowercase


INITIAL_BITS = 8
BITS = 5
LAST_NUM = 2**BITS
N = LAST_NUM - 26
idxs_of_letters = {
    ch: i for ch, i in zip(ascii_lowercase, range(N, LAST_NUM))
}
letters_by_idcs = {
    i: ch for ch, i in zip(ascii_lowercase, range(N, LAST_NUM))
}
TRIE = {}
TRIE[0] = 0
WORDS = [""]


def convert_idx(i):
    res = []
    while i:
        i, r = divmod(i, N)
        res.append(r)
    res.reverse()
    return res


def pack(s):
    cur = TRIE
    res = []
    for ch in s:
        if ch in cur:
            cur = cur[ch]
        else:
            res.extend(convert_idx(cur[0]))
            res.append(idxs_of_letters[ch])
            cur[ch] = {}
            cur[ch][0] = len(WORDS)
            WORDS.append(WORDS[cur[0]] + ch if 0 in cur else ch)
            cur = TRIE
    if not cur is TRIE:
        res.extend(convert_idx(cur[0]))

    bit_sequence = 0
    for num in res:
        bit_sequence = (bit_sequence << BITS) | num
    # bit_sequence <<= INITIAL_BITS - (len(res) * BITS % INITIAL_BITS)
    res = []
    word = (1 << INITIAL_BITS) - 1
    while bit_sequence:
        res.append(bit_sequence & word)
        bit_sequence >>= INITIAL_BITS

    print(f"Compression rate: {len(res) / len(s)}")
    print(f"Dict len: {len(WORDS)}")
    print(f"Letters left: {sum(chunk >= N for chunk in res)}")
    return res


def unpack(s):
    bit_sequence = 0
    for chunk in map(int, reversed(s.split())):
        bit_sequence = (bit_sequence << INITIAL_BITS) | chunk
    s = []
    word = (1 << BITS) - 1
    while bit_sequence:
        s.append(bit_sequence & word)
        bit_sequence >>= BITS
    s.reverse()

    res = []
    prev_word_idx = 0
    for chunk in s:
        if chunk >= N:
            WORDS.append(WORDS[prev_word_idx] + letters_by_idcs[chunk])
            prev_word_idx = 0
            res.append(WORDS[-1])
        else:
            prev_word_idx = prev_word_idx * N + chunk
    if prev_word_idx:
        res.append(WORDS[prev_word_idx])
    return "".join(res)


def main():
    op = input()
    if op == "pack":
        print(*pack(input()))
    else:
        print(unpack(input()))


def test():
    with open("j_tests.txt") as file:
        for _ in range(6):
            s = file.readline().strip()
            res = " ".join(map(str, pack(s)))
            s_ = unpack(res)
            print("Strings match" if s == s_ else "Strings do not match")
            print("=" * 20)


if __name__ == "__main__":
    # main()
    test()


##############################################
    


from string import ascii_lowercase


BITS = 8
idxs_of_letters = {
    ch: i for i, ch in enumerate(ascii_lowercase)
}
letters_by_idcs = {
    i: ch for i, ch in enumerate(ascii_lowercase)
}
TRIE = {}
TRIE[0] = 0
WORDS = [""]


def pack(s):
    cur_trie = TRIE
    bit_sequence = 1
    prev_word_idx_bits = 1
    for ch in s:
        if ch in cur_trie:
            cur_trie = cur_trie[ch]
        else:
            bit_sequence <<= prev_word_idx_bits
            bit_sequence |= cur_trie[0]
            bit_sequence <<= 5
            bit_sequence |= idxs_of_letters[ch]
            cur_trie[ch] = {}
            cur_trie[ch][0] = len(WORDS)
            WORDS.append(WORDS[cur_trie[0]] + ch)
            if len(WORDS) == (1 << prev_word_idx_bits):
                prev_word_idx_bits += 1
            cur_trie = TRIE
    if not cur_trie is TRIE:
        bit_sequence <<= prev_word_idx_bits
        bit_sequence |= cur_trie[0]
    bit_sequence <<= 1
    bit_sequence |= 1

    res = []
    chunk = (1 << BITS) - 1
    while bit_sequence:
        res.append(bit_sequence & chunk)
        bit_sequence >>= BITS
    return res


def unpack(s: str):
    bit_sequence = 0
    for chunk in map(int, reversed(s.split())):
        bit_sequence <<= BITS
        bit_sequence |= chunk
    bit_sequence >>= 1

    prev_word_idx_bits = 1
    prev_word_idx_mask = 1
    letter_bits = 5
    letter_mask = (1 << 5) - 1
    res = []
    shift = bit_sequence.bit_length() - 1
    while True:
        shift -= prev_word_idx_bits
        if shift < 0:
            break
        prev_word_idx = (bit_sequence >> shift) & prev_word_idx_mask
        res.append(WORDS[prev_word_idx])

        shift -= letter_bits
        if shift < 0:
            break
        letter_idx = (bit_sequence >> shift) & letter_mask
        res.append(letters_by_idcs[letter_idx])

        WORDS.append(WORDS[prev_word_idx] + letters_by_idcs[letter_idx])
        if len(WORDS) == (1 << prev_word_idx_bits):
            prev_word_idx_bits += 1
            prev_word_idx_mask = (prev_word_idx_mask << 1) + 1

    return "".join(res)


def main():
    op = input()
    if op == "pack":
        res = pack(input())
        print(len(res))
        print(*res, flush=True)
    else:
        _ = input()
        res = unpack(input())
        print(res)


def test():
    import time


    test_cnt = 6
    with open("/home/marat/yandex_training_7/pset3_bit_ops_hamming_code_compression/j_tests.txt") as file:
        for i in range(test_cnt):
            start = time.time()
            s = file.readline().strip()
            res = " ".join(map(str, pack(s)))
            WORDS.clear()
            WORDS.append("")
            TRIE.clear()
            TRIE[0] = 0
            finish = time.time()
            print(f"pack time: {finish - start}")
            start = time.time()
            s_ = unpack(res)
            WORDS.clear()
            WORDS.append("")
            TRIE.clear()
            TRIE[0] = 0
            finish = time.time()
            print(f"unpack time: {finish - start}")
            print("Strings match" if s == s_ else "Strings do not match")
            print("=" * 20)


if __name__ == "__main__":
    main()
    # test()


##########################################
    

from string import ascii_lowercase


BITS = 8
idxs_of_letters = {
    ch: i for i, ch in enumerate(ascii_lowercase)
}
letters_by_idcs = {
    i: ch for i, ch in enumerate(ascii_lowercase)
}
TRIE = {}
TRIE[0] = 0
WORDS = [""]


def pack(s):
    cur_trie = TRIE
    bit_sequence = ["1"]
    prev_word_idx_bits = 1
    for ch in s:
        if ch in cur_trie:
            cur_trie = cur_trie[ch]
        else:
            bit_sequence.append(bin(cur_trie[0])[2:].rjust(prev_word_idx_bits, "0"))
            bit_sequence.append(bin(idxs_of_letters[ch])[2:].rjust(5, "0"))
            cur_trie[ch] = {}
            cur_trie[ch][0] = len(WORDS)
            WORDS.append(WORDS[cur_trie[0]] + ch)
            if len(WORDS) == (1 << prev_word_idx_bits):
                prev_word_idx_bits += 1
            cur_trie = TRIE
    if not cur_trie is TRIE:
        bit_sequence.append(bin(cur_trie[0])[2:].rjust(prev_word_idx_bits, "0"))
    bit_sequence = "".join(bit_sequence)
    bit_sequence = "0" * (BITS - len(bit_sequence) % BITS) + bit_sequence

    res = [int(bit_sequence[i:i + BITS], 2) for i in range(0, len(bit_sequence), BITS)]
    print(f"Compression rate: {len(res) / len(s)}")
    print(f"Dict len: {len(WORDS)}")

    return res


def unpack(s: str):
    bit_sequence = "".join(
        bin(int(chunk))[2:].rjust(BITS, "0")
        for chunk in s.split()
    )

    prev_word_idx_bits = 1
    letter_bits = 5
    res = []
    i = 0
    while bit_sequence[i] == "0":
        i += 1
    i += 1
    n = len(bit_sequence)
    while True:
        j = i + prev_word_idx_bits
        prev_word_idx = int(bit_sequence[i:j], 2)
        res.append(WORDS[prev_word_idx])
        if j == n:
            break
        i = j

        j = i + letter_bits
        letter_idx = int(bit_sequence[i:j], 2)
        res.append(letters_by_idcs[letter_idx])
        if j == n:
            break
        i = j

        WORDS.append(WORDS[prev_word_idx] + letters_by_idcs[letter_idx])
        if len(WORDS) == (1 << prev_word_idx_bits):
            prev_word_idx_bits += 1

    return "".join(res)


def main():
    op = input()
    if op == "pack":
        res = pack(input())
        print(len(res))
        print(*res, flush=True)
    else:
        _ = input()
        res = unpack(input())
        print(res)


def test():
    import time


    test_cnt = 6
    with open("/home/marat/yandex_training_7/pset3_bit_ops_hamming_code_compression/j_tests.txt") as file:
        for i in range(test_cnt):
            start = time.time()
            s = file.readline().strip()
            # print(s)
            res = " ".join(map(str, pack(s)))
            WORDS.clear()
            WORDS.append("")
            TRIE.clear()
            TRIE[0] = 0
            finish = time.time()
            print(f"pack time: {finish - start}")
            start = time.time()
            s_ = unpack(res)
            # print(s_)
            WORDS.clear()
            WORDS.append("")
            TRIE.clear()
            TRIE[0] = 0
            finish = time.time()
            print(f"unpack time: {finish - start}")
            print("Strings match" if s == s_ else "Strings do not match")
            print("=" * 20)


if __name__ == "__main__":
    # main()
    test()
