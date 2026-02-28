import random
from string import ascii_lowercase


N = 200_000
strings = []
s = [ch for ch in ascii_lowercase]
cur_len = 26
for s_ in s:
    for ch in ascii_lowercase:
        s.append(s_ + ch)
        cur_len += len(s[-1])
        if cur_len >= N:
            break
    if cur_len >= N:
        break
strings.append("".join(s))
strings.append("a" * N)
strings.append("".join(random.choice(ascii_lowercase) for _ in range(N)))

with open("j_tests.txt", "w") as file:
    for s in strings:
        file.write(s + "\n")
