def main():
    n, m = map(int, input().split())
    cur = 1
    for w in map(int, input().split()):
        cur |= cur << w
    
    cur = cur & ((1 << m + 1) - 1)
    print(len(bin(cur)) - 3)


if __name__ == "__main__":
    main()
