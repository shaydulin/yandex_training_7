from collections import defaultdict


def main():
    N = 30

    m = int(input())
    t = list(map(int, input().split()))
    cost = [1 << i for i in range(N + 1)]
    cur = {m: 0}
    ans = float("inf")
    seen = defaultdict(lambda: float("inf"))
    while cur:
        nxt = defaultdict(lambda: float("inf"))
        for m_ in cur:
            for i in range(N + 1):
                res, rem = divmod(m_, t[i])
                if rem:
                    if (new_cost := cur[m_] + res * cost[i]) < seen[rem]:
                        nxt[rem] = min(nxt[rem], new_cost)
                        seen[rem] = new_cost
                    ans = min(ans, cur[m_] + (res + 1) * cost[i])
                else:
                    ans = min(ans, cur[m_] + res * cost[i])
        cur = nxt

    print(ans)


if __name__ == "__main__":
    main()
