from itertools import count


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.zero = k - 1
        self.mx_tree = [float("-inf")] * (k * 2 - 1)
        self.mx_tree[self.zero:self.zero + n] = nums

        for i in range(k - 2, -1, -1):
            self.calc_for_idx(i)

    def update_element(self, i, val):
        i += self.zero
        self.mx_tree[i] = val
        while (i := (i - 1) // 2) >= 0:
            self.calc_for_idx(i)

    def calc_for_idx(self, i):
        self.mx_tree[i] = max(self.mx_tree[i * 2 + 1], self.mx_tree[i * 2 + 2])

    def get_closest_right_larger(self, l, x):
        return self.traversal(0, x, l, 0, (len(self.mx_tree) + 1) // 2)

    def traversal(self, i, x, l, cur_l, cur_r):
        if self.mx_tree[i] < x:
            return -1
        if cur_r <= l:
            return -1
        if cur_r - cur_l == 1:
            return cur_l

        idx_l = self.traversal(i * 2 + 1, x, l, cur_l, (cur_l + cur_r) // 2)
        if idx_l != -1:
            return idx_l

        idx_r = self.traversal(i * 2 + 2, x, l, (cur_l + cur_r) // 2, cur_r)
        if idx_r != -1:
            return idx_r

        return -1


def main():
    n, m = map(int, input().split())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    ans = []
    for _ in range(m):
        t, i, x = map(int, input().split())
        if t == 0:
            tree.update_element(i - 1, x)
        else:
            res = tree.get_closest_right_larger(i - 1, x)
            ans.append(res + 1 if res != -1 else res)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
