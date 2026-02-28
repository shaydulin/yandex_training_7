from collections import deque


def main():
    n = int(input())
    num = deque(bin(n)[2:])
    ans = n
    for _ in range(len(num)):
        num.appendleft(num.pop())
        ans = max(ans, int("".join(num), 2))
    print(ans)


if __name__ == "__main__":
    main()
