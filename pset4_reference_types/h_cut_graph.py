class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.cnt = [1] * n

    def union(self, u, v):
        root_u = self.find_root(u)
        root_v = self.find_root(v)
        if root_u != root_v:
            if self.cnt[root_u] < self.cnt[root_v]:
                self.root[root_u] = root_v
                self.cnt[root_v] += self.cnt[root_u]
            else:
                self.root[root_v] = root_u
                self.cnt[root_u] += self.cnt[root_v]

    def find_root(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find_root(self.root[u])
        return self.root[u]

    def check(self, u, v):
        return self.find_root(u) == self.find_root(v)


def main():
    data = open("input.txt").readlines()

    n, m, k = map(int, data[0].split())
    uf = UnionFind(n + 1)

    ans = []
    for _, q in zip(range(k), map(str.split, reversed(data))):
        if q[0] == "cut":
            uf.union(int(q[1]), int(q[2]))
        else:
            ans.append("YES" if uf.check(int(q[1]), int(q[2])) else "NO")

    print("\n".join(reversed(ans)))

if __name__ == "__main__":
    main()
