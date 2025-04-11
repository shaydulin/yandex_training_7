def main():
    n, d = map(int, input().split())
    items = []
    for _ in range(n):
        title, m = input().split()
        items.append((title, int(m)))
    items.sort(key=lambda item: item[1])
    # print(items)

    inf = float("inf")
    mx_materiality = max(item[1] for item in items)
    refused_materiality = [inf] * (mx_materiality + 1)
    refused_materiality[0] = 0
    days = 0
    refused_items = []
    for title, m_i in items:
        needed_m = max(0, m_i - d)
        m = min((m for m in range(needed_m, m_i)), key=lambda m: refused_materiality[m])
        if refused_materiality[m] == inf:
            break

        refused_items.append(title)
        days_to_add_cur_materiality = 1 + refused_materiality[m]
        days += days_to_add_cur_materiality
        for m in range(mx_materiality - m_i, -1, -1):
            refused_materiality[m + m_i] = min(refused_materiality[m + m_i], refused_materiality[m] + days_to_add_cur_materiality)

    # print(refused_materiality)
    print(len(refused_items), days)
    for item in sorted(refused_items):
        print(item)


if __name__ == "__main__":
    main()
