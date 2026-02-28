class Fenwick3D:
    def __init__(self, n):
        self.n = n
        self.fenwick = [
            [[0] * n for _ in range(n)]
            for _ in range(n)
        ]
        self.res = 0

    def get_sum_in_region(self, x1, y1, z1, x2, y2, z2):
        x1 -= 1
        y1 -= 1
        z1 -= 1
        x1, x2 = self.get_idcs(x1, x2)
        y1, y2 = self.get_idcs(y1, y2)
        z1, z2 = self.get_idcs(z1, z2)

        self.count_regions(x2, y2, z2, 1)

        self.count_regions(x1, y2, z2, -1)
        self.count_regions(x2, y1, z2, -1)
        self.count_regions(x2, y2, z1, -1)

        self.count_regions(x1, y1, z2, 1)
        self.count_regions(x1, y2, z1, 1)
        self.count_regions(x2, y1, z1, 1)

        self.count_regions(x1, y1, z1, -1)

        res = self.res
        self.res = 0

        return res

    def count_regions(self, idcs_x, idcs_y, idcs_z, addition):
        self.res += addition * sum(self.fenwick[x][y][z] for x in idcs_x for y in idcs_y for z in idcs_z)

    def get_idcs(self, i1, i2):
        idcs1 = []
        idcs2 = []
        while i1 != i2:
            if i1 > i2:
                idcs1.append(i1)
                i1 = (i1 & i1 + 1) - 1
            else:
                idcs2.append(i2)
                i2 = (i2 & i2 + 1) - 1
        return idcs1, idcs2

    def add_to_element(self, x, y, z, val):
        xs, ys, zs = [], [], []
        while x < self.n:
            xs.append(x)
            x |= x + 1
        while y < self.n:
            ys.append(y)
            y |= y + 1
        while z < self.n:
            zs.append(z)
            z |= z + 1

        for x in xs:
            for y in ys:
                for z in zs:
                    self.fenwick[x][y][z] += val


def main():
    ans = []
    with open("input.xt") as file:
        n = int(file.readline())
        fw = Fenwick3D(n)
        while True:
            q = list(map(int, file.readline().split()))
            if q[0] == 1:
                fw.add_to_element(*q[1:])
            elif q[0] == 2:
                ans.append(fw.get_sum_in_region(*q[1:]))
            else:
                break

    with open("output.txt", "w") as file:
        file.write("\n".join(map(str, ans)))


# def main():
#     ans = []

#     n = int(sys.stdin.readline())
#     fw = Fenwick3D(n)

#     data = sys.stdin.read().split("\n")
#     for q in data:
#         q = list(map(int, q.split()))
#         if q[0] == 1:
#             fw.add_to_element(*q[1:])
#         elif q[0] == 2:
#             ans.append(fw.get_sum_in_region(*q[1:]))
#         else:
#             break

#     print(*ans)


if __name__ == "__main__":
    main()
