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


if __name__ == "__main__":
    main()
