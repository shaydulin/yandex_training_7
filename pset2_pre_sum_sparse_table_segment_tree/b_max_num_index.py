# segment tree solution
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
        return self.traversal(0, l, r, 0, (len(self.mx_tree) + 1) // 2)[1]

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


def main_segment_tree():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    k = int(input())
    ans = []
    for _ in range(k):
        l, r = map(int, input().split())
        ans.append(tree.get_mx_idx(l - 1, r))
    print("\n".join(map(str, ans)))


class SparseTable:
    def __init__(self, n, nums):
        self.nums = nums
        self.table = [[*range(n)]]
        prev_len = 1
        cur_len = 2
        while cur_len < n:
            self.table.append([])
            cur, prev = self.table[-1], self.table[-2]
            for i in range(n - cur_len + 1):
                cur.append(
                    prev[i]
                    if nums[prev[i]] >= nums[prev[i + prev_len]]
                    else prev[i + prev_len]
                )
            prev_len, cur_len = cur_len, cur_len * 2
        # for row in self.table:
        #     print(row)

        self.exp = []
        cur = 0
        nxt = 1
        for i in range(n + 1):
            self.exp.append(cur)
            if i == 2**nxt:
                cur, nxt = nxt, nxt + 1
        # print(exp)
    
    def get_mx_idx(self, l, r):
        exp = self.exp[r - l]
        idcs = self.table[exp]
        left = idcs[l]
        right = idcs[r - 2**exp]
        return (
            left
            if self.nums[left] >= self.nums[right]
            else right
        )


def main_sparse_table():
    n = int(input())

    nums = list(map(int, input().split()))
    table = SparseTable(n, nums)

    k = int(input())
    ans = []
    for _ in range(k):
        l, r = map(int, input().split())
        ans.append(table.get_mx_idx(l - 1, r) + 1)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main_sparse_table()
