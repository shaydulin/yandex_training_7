from itertools import count


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.zero = k - 1
        self.mn_tree = [float("inf")] * (k * 2 - 1)
        self.mn_tree[self.zero:self.zero + n] = nums
        self.mn_cnt = [1] * (k * 2 - 1)

        for i in range(k - 2, -1, -1):
            self.calc_for_idx(i)

    def update_element(self, i, val):
        i += self.zero
        self.mn_tree[i] = val
        while (i := (i - 1) // 2) >= 0:
            self.calc_for_idx(i)

    def calc_for_idx(self, i):
        if self.mn_tree[i * 2 + 1] < self.mn_tree[i * 2 + 2]:
            self.mn_tree[i] = self.mn_tree[i * 2 + 1]
            self.mn_cnt[i] = self.mn_cnt[i * 2 + 1]
        elif self.mn_tree[i * 2 + 1] > self.mn_tree[i * 2 + 2]:
            self.mn_tree[i] = self.mn_tree[i * 2 + 2]
            self.mn_cnt[i] = self.mn_cnt[i * 2 + 2]
        else:
            self.mn_tree[i] = self.mn_tree[i * 2 + 1]
            self.mn_cnt[i] = self.mn_cnt[i * 2 + 1] + self.mn_cnt[i * 2 + 2]

    def get_idx_of_kth_zero(self, l, r, k):
        res = self.traversal(0, k, l, r, 0, (len(self.mn_tree) + 1) // 2)[1]
        return res - self.zero + 1 if res != -1 else res

    def traversal(self, i, k, l, r, cur_l, cur_r):
        if self.mn_tree[i] > 0:
            return 0, -1
        if cur_l >= r or cur_r <= l:
            return 0, -1
        if l <= cur_l and cur_r <= r:
            if self.mn_cnt[i] < k:
                return self.mn_cnt[i], -1
            elif cur_r - cur_l == 1 and self.mn_cnt[i] == k:
                return 1, i
        
        zero_cnt_l, idx_l = self.traversal(i * 2 + 1, k, l, r, cur_l, (cur_l + cur_r) // 2)
        if idx_l != -1:
            return zero_cnt_l, idx_l
        
        zero_cnt_r, idx_r = self.traversal(i * 2 + 2, k - zero_cnt_l, l, r, (cur_l + cur_r) // 2, cur_r)
        if idx_r != -1:
            return zero_cnt_r, idx_r
        
        return zero_cnt_l + zero_cnt_r, -1


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    k = int(input())
    ans = []
    for _ in range(k):
        q = input().split()
        if q[0] == "u":
            tree.update_element(int(q[1]) - 1, int(q[2]))
        else:
            ans.append(tree.get_idx_of_kth_zero(int(q[1]) - 1, int(q[2]), int(q[3])))
    print(*ans)


if __name__ == "__main__":
    main()
