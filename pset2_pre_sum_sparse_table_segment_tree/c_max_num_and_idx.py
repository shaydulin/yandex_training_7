from itertools import count


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.mx_tree = [float("-inf")] * (k * 2 - 1)
        self.mx_tree[k - 1:k - 1 + n] = nums
        self.mx_idx = [-1] * (k * 2 - 1)
        self.mx_idx[k - 1:k - 1 + n] = [*range(1, n + 1)]

        for i in range(k - 2, -1, -1):
            if self.mx_tree[i * 2 + 1] > self.mx_tree[i * 2 + 2]:
                self.mx_tree[i] = self.mx_tree[i * 2 + 1]
                self.mx_idx[i] = self.mx_idx[i * 2 + 1]
            else:
                self.mx_tree[i] = self.mx_tree[i * 2 + 2]
                self.mx_idx[i] = self.mx_idx[i * 2 + 2]

    def get_mx_idx(self, l, r):
        return self.traversal(0, l, r, 0, (len(self.mx_tree) + 1) // 2)

    def traversal(self, i, l, r, cur_l, cur_r):
        if l <= cur_l and cur_r <= r:
            return self.mx_tree[i], self.mx_idx[i]
        elif cur_l >= r or cur_r <= l:
            return float("-inf"), -1
        mx_left, idx_left = self.traversal(i * 2 + 1, l, r, cur_l, (cur_l + cur_r) // 2)
        mx_right, idx_right = self.traversal(i * 2 + 2, l, r, (cur_l + cur_r) // 2, cur_r)
        if mx_left > mx_right:
            return mx_left, idx_left
        else:
            return mx_right, idx_right


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        print(*tree.get_mx_idx(l - 1, r))


if __name__ == "__main__":
    main()
