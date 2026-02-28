def main():
    # n = int(input())
    n = int(open(0).readline())

    ans = 0
    while n:
        ans += n & 1
        n >>= 1

    print(ans)


if __name__ == "__main__":
    main()
