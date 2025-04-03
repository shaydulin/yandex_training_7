def main():
    N = 3
    n = int(input())
    cur = [0] * N
    cur[0] = 1
    for _ in range(n):
        nxt = [0] * N
        nxt[0] += sum(cur)
        for i in range(N - 1):
            nxt[i + 1] += cur[i]

        cur = nxt

    print(sum(cur))


if __name__ == "__main__":
    main()