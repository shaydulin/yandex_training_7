def main():
    n, m = map(int, input().split())
    mx_cost = [[[0, None] for _ in range(m + 1)]]
    mx_cost[0][0][1] = -1
    items = [*zip(map(int, input().split()), map(int, input().split()))]
    for item, (w, c) in enumerate(items):
        mx_cost.append(mx_cost[-1].copy())
        cur = mx_cost[-1]
        for i in range(m - w, -1, -1):
            if cur[i][1] is not None and cur[i][0] + c > cur[i + w][0]:
                cur[i + w] = [cur[i][0] + c, item]

    i = len(mx_cost) - 1
    j = max((j for j in range(m + 1) if mx_cost[i][j][1] is not None), key=lambda j: mx_cost[i][j][0])
    ans = []
    while (item := mx_cost[i][j][1]) != -1:
        ans.append(item + 1)
        i = item
        j = j - items[item][0]

    for item in reversed(ans):
        print(item)


if __name__ == "__main__":
    main()
