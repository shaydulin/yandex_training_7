from collections import deque


def main():
    n = int(input())
    cost = deque([0, float("inf"), float("inf")])
    for _ in range(n):
        cur = cost.popleft()
        a, b, c = map(int, input().split())
        cost[0] = min(cost[0], cur + a)
        cost[1] = min(cost[1], cur + b)
        cost.append(cur + c)
    print(cost[0])


if __name__ == "__main__":
    main()