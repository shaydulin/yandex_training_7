from collections import defaultdict
from functools import reduce
from itertools import count
import operator


def main():
    n, k = map(int, input().split())
    poss_lens = defaultdict(lambda: 1)
    bricks = [tuple(map(int, input().split())) for _ in range(n)]
    bricks_by_color = [[] for _ in range(k)]
    for i, (l, c) in enumerate(bricks):
        poss_lens[c] |= poss_lens[c] << l
        bricks_by_color[c - 1].append(i)
    edges: int = reduce(operator.and_, poss_lens.values())

    if edges.bit_count() < 3:
        print("NO")
        return

    print("YES")
    length = next(i for i in count(1) if edges & 1 << i)
    res = []
    for c in range(k):
        res.extend(build_row(length, bricks_by_color[c], bricks))
    print(*res)


def build_row(length, idcs, bricks):
    dp = [-1] * (length + 1)
    dp[0] = 0
    for i in idcs:
        l = bricks[i][0]
        if l > length:
            continue
        for j in range(length - l, -1, -1):
            if dp[j] == -1 or dp[j + l] != -1:
                continue
            dp[j + l] = i
    res = []
    i = length
    while i:
        res.append(dp[i] + 1)
        i -= bricks[dp[i]][0]
    return res


if __name__ == "__main__":
    main()
