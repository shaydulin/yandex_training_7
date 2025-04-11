def main():
    N, S = map(int, input().split())
    items = []
    for _ in range(N):
        # v, c, p
        items.append(tuple(map(int, input().split())))
    idcs = sorted(range(N), key=lambda i: -items[i][2])

    V = sum(item[0] for item in items)
    mx_cost = [[[0, None] for _ in range(V + 1)]]
    mx_cost[0][0][1] = -1
    for idx in range(N):
        v, c, p = items[idcs[idx]]
        mx_cost.append(mx_cost[-1].copy())
        cur = mx_cost[-1]
        mx_volume = min(S + p - v, V - v)
        for i in range(mx_volume, -1, -1):
            if cur[i][1] is not None and cur[i][0] + c > cur[i + v][0]:
                cur[i + v] = [cur[i][0] + c, idx]

    i = len(mx_cost) - 1
    j = max((j for j in range(V + 1) if mx_cost[i][j][1] is not None), key=lambda j: mx_cost[i][j][0])
    cost = mx_cost[i][j][0]
    ans = []
    while (idx_in_idcs := mx_cost[i][j][1]) != -1:
        item = idcs[idx_in_idcs]
        ans.append(item + 1)
        i = idx_in_idcs
        j = j - items[item][0]
    ans.sort()

    print(len(ans), cost)
    print(*ans)


if __name__ == "__main__":
    main()
