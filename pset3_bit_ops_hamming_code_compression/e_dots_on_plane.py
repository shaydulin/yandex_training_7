def main():
    x, y = map(int, input().split())
    print(x ^ y)
    x, c = map(int, input().split())
    print(x ^ c)


def draw(n):
    grid = [[None] * n for _ in range(n)]
    grid[0][0] = 0
    for i in range(n):
        for j in range(n):
            nums = set(grid[i][k] for k in range(j)) | set(grid[k][j] for k in range(i))
            cur = next(num for num in range(1000) if num not in nums)
            print(cur == i ^ j)
            grid[i][j] = cur
    
    for row in grid:
        print("  ".join(str(num).rjust(2) for num in row))
        # print("  ".join(bin(num)[2:].rjust(5) for num in row))


if __name__ == "__main__":
    main()
