from itertools import accumulate


def main():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]

    table[0] = [*accumulate(table[0])]
    for i in range(1, n):
        table[i][0] += table[i - 1][0]
    
    for i in range(1, n):
        for j in range(1, m):
            table[i][j] += max(table[i - 1][j], table[i][j - 1])
    
    print(table[-1][-1])

    i, j = n - 1, m - 1
    path = []
    while i and j:
        if table[i - 1][j] > table[i][j - 1]:
            i -= 1
            path.append("D")
        else:
            j -= 1
            path.append("R")
    while i:
        i -= 1
        path.append("D")
    while j:
        j -= 1
        path.append("R")
    
    print(" ".join(reversed(path)))

if __name__ == "__main__":
    main()