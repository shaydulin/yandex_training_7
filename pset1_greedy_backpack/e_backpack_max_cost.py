def main():
    n, m = map(int, input().split())
    mx_cost = [-1] * (m + 1)
    mx_cost[0] = 0
    for w, c in zip(map(int, input().split()), map(int, input().split())):
        for i in range(m - w, -1, -1):
            mx_cost[i + w] = max(mx_cost[i + w], mx_cost[i] + c)

    print(max(mx_cost))


if __name__ == "__main__":
    main()
