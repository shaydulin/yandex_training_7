def main():
    n = int(input())
    cur = {0: (0, 0, 0)}
    for day in range(1, n + 1):
        price = int(input())
        nxt = {}
        for spent, (coupons_left, coupons_spent, days) in cur.items():
            if price > 100:
                add_item(nxt, spent + price, (coupons_left + 1, coupons_spent, days))
            else:
                add_item(nxt, spent + price, (coupons_left, coupons_spent, days))

            if coupons_left:
                add_item(nxt, spent, (coupons_left - 1, coupons_spent + 1, days | 1 << day))
        cur = nxt

    mn_price = min(cur)
    print(mn_price)
    coupons_left, coupons_spent, days = cur[mn_price]
    print(coupons_left, coupons_spent)
    for day in range(1, n + 1):
        if days & 1 << day:
            print(day)



def add_item(nxt, new_spent, data):
    if new_spent not in nxt or data[0] > nxt[new_spent][0]:
        nxt[new_spent] = data


if __name__ == "__main__":
    main()