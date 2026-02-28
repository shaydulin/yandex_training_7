def main():
    f = open(0)
    n, k = map(int, f.readline().split())
    field_x = [0] * n
    field_y = [0] * n
    field_z = [0] * n
    for _ in range(k):
        x, y, z = map(int, f.readline().split())
        x -= 1
        y -= 1
        z -= 1
        field_x[z] |= 1 << y
        field_y[z] |= 1 << x
        field_z[x] |= 1 << y

    # invert
    full = (1 << n) - 1
    for i in range(n):
        field_x[i] ^= full
        field_y[i] ^= full
        field_z[i] ^= full

    for x in range(n):
        if not field_z[x]:
            continue
        for z in range(n):
            if not field_x[z]:
                continue
            if not (holes := field_z[x] & field_x[z]):
                continue
            if field_y[z] & 1 << x:
                print("NO")
                print(x + 1, next(y for y in range(n) if holes & 1 << y) + 1, z + 1)
                return

    print("YES")


if __name__ == "__main__":
    main()
