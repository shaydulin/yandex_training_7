import sys


sys.setrecursionlimit(100000)


def main():
    n = int(input())
    tree: list[set] = [set() for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].add(v)
        tree[v].add(u)

    ans = [0] * (n + 1)

    def traversal(parent):
        total = 1
        for child in tree[parent]:
            tree[child].remove(parent)
            total += traversal(child)
        ans[parent] = total
        return total
    
    traversal(1)

    print(*ans[1:])


if __name__ == "__main__":
    main()