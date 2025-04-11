def main():
    n = int(input())

    ans = []
    cur_len = 0
    mx_len = float("inf")
    for num in map(int, input().split()):
        if cur_len + 1 <= mx_len and num >= cur_len + 1:
            cur_len += 1
            mx_len = min(mx_len, num)
        else:
            ans.append(cur_len)
            cur_len = 1
            mx_len = num
    ans.append(cur_len)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()
