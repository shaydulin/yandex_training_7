def main():
    n = int(input())
    tree = {}
    for _ in range(n - 1):
        child, parent = input().split()
        tree[child] = parent
    
    ans = {}
    for child in tree:
        if child not in ans:
            dfs(ans, tree, child)

    for person in sorted(ans):
        print(person, ans[person])


def dfs(ans, tree, child):
    if child not in tree:
        ans[child] = 0
    else:
        ans[child] = 1 + dfs(ans, tree, tree[child])
    return ans[child]


if __name__ == "__main__":
    main()