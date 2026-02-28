def main():
    data = open("input.txt").readlines()

    n = int(data[0])
    ranks = list(map(int, data[1].split()))
    left = [i - 1 for i in range(n)]
    left[0] = n - 1
    right = [i + 1 for i in range(n)]
    right[-1] = 0

    ans = [0] * n
    rnd = 1
    cur = [*range(n)]
    while cur and n > 2:
        nxt = set()
        removed = []

        for i in cur:
            l, r = left[i], right[i]
            if ranks[i] < ranks[l] and ranks[i] < ranks[r]:
                ans[i] = rnd
                removed.append(i)
        n -= len(removed)
        for i in removed:
            l, r = left[i], right[i]
            right[l] = r
            left[r] = l
            nxt.add(l)
            nxt.add(r)

        cur = nxt
        rnd += 1

    print(*ans)


if __name__ == "__main__":
    main()
