class UnionFind:
    def __init__(self, n):
        self.root = [*range(n)]
        self.cnt = [1] * n

    def union(self, u, v):
        root_u = self.find_root(u)
        root_v = self.find_root(v)
        if root_u == root_v:
            return self.cnt[root_u]
        if self.cnt[root_u] < self.cnt[root_v]:
            self.root[root_u] = root_v
            self.cnt[root_v] += self.cnt[root_u]
            return self.cnt[root_v]
        else:
            self.root[root_v] = root_u
            self.cnt[root_u] += self.cnt[root_v]
            return self.cnt[root_u]

    def find_root(self, u):
        if self.root[u] == u:
            return u
        self.root[u] = self.find_root(self.root[u])
        return self.root[u]
        

def main():
    data = open("input.txt").readlines()

    n, m = map(int, data[0].split())
    uf = UnionFind(n + 1)
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        cnt = uf.union(u, v)
        if cnt == n:
            print(i)
            return


if __name__ == "__main__":
    main()
