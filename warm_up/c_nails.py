from itertools import pairwise


def main():
    n = int(input())
    coords = sorted(map(int, input().split()))
    dist = [b - a for a, b in pairwise(coords)]
    res = [0, float("inf")]
    for d in dist:
        res = [res[1], min(res) + d]
    print(res[1])


if __name__ == "__main__":
    main()