from itertools import count
import array


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.mx_tree = array.array("I", [0] * (k * 2 - 1))
        self.mx_tree[k - 1:k - 1 + n] = array.array("I", nums)
        self.to_add = array.array("I", [0] * (k * 2 - 1))

        for i in range(k - 2, -1, -1):
            self.mx_tree[i] = max(self.mx_tree[i * 2 + 1], self.mx_tree[i * 2 + 2])

    def get_mx(self, l, r):
        return self.traversal(0, l, r, 0, 0, (len(self.mx_tree) + 1) // 2)[1]

    def add_on_segment(self, l, r, val):
        self.traversal(0, l, r, val, 0, (len(self.mx_tree) + 1) // 2)

    def traversal(self, i, l, r, val, cur_l, cur_r):
        if cur_l >= r or cur_r <= l:
            return self.mx_tree[i] + self.to_add[i], 0

        if l <= cur_l and cur_r <= r:
            self.to_add[i] += val
            return self.mx_tree[i] + self.to_add[i], self.mx_tree[i] + self.to_add[i]

        self.to_add[i * 2 + 1] += self.to_add[i]
        self.to_add[i * 2 + 2] += self.to_add[i]
        self.to_add[i] = 0
        mx_l, mx_l_cur = self.traversal(i * 2 + 1, l, r, val, cur_l, (cur_l + cur_r) // 2)
        mx_r, mx_r_cur = self.traversal(i * 2 + 2, l, r, val, (cur_l + cur_r) // 2, cur_r)
        self.mx_tree[i] = max(mx_l, mx_r)
        return self.mx_tree[i], max(mx_l_cur, mx_r_cur)


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    m = int(input())
    ans = []
    for _ in range(m):
        q = input().split()
        if q[0] == "a":
            tree.add_on_segment(int(q[1]) - 1, int(q[2]), int(q[3]))
        else:
            ans.append(tree.get_mx(int(q[1]) - 1, int(q[2])))
    print(*ans)


if __name__ == "__main__":
    main()
