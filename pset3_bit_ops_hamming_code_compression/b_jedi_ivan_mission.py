def main():
    n = int(input())

    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    ans = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            ans[i] |= mat[i][j]
            ans[j] |= mat[i][j]

    print(*ans)


if __name__ == "__main__":
    main()
