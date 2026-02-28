def main():
    data = open(0).readlines()

    n = int(data[0])
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        j = int(data[i])
        graph[i].append(j)
        graph[j].append(i)

    def bfs(i):
        cur = [i]
        seen[i] = 1
        while cur:
            nxt = []
            for i in cur:
                for j in graph[i]:
                    if seen[j]:
                        continue
                    seen[j] = 1
                    nxt.append(j)
            cur = nxt

    ans = 0
    seen = [0] * (n + 1)
    for i in range(1, n + 1):
        if seen[i]:
            continue
        bfs(i)
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
