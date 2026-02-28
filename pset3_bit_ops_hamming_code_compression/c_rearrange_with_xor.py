from heapq import nlargest
from itertools import cycle


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    bit_len = max(num.bit_length() for num in nums)
    bit_cnt = [num.bit_count() for num in nums]

    ans = [0] * n
    seen = [0] * bit_len
    miss = 0
    for bit in cycle(range(bit_len)):
        idcs = nlargest(
            2,
            (i for i in range(n) if bit_cnt[i] and not seen[bit] & 1 << i),
            key=lambda i: bit_cnt[i]
        )
        if len(idcs) < 2:
            miss += 1
            if miss == bit_len:
                print("impossible")
                return
            continue
        else:
            miss = 0
        i, j = idcs
        bit_cnt[i] -= 1
        bit_cnt[j] -= 1
        ans[i] |= 1 << bit
        ans[j] |= 1 << bit
        seen[bit] |= 1 << i
        seen[bit] |= 1 << j
        if sum(bit_cnt) == 0:
            break

    print(*ans)


if __name__ == "__main__":
    main()
