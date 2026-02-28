from itertools import count


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.mx_tree = [float("-inf")] * (k * 2 - 1)
        self.mx_tree[k - 1:k - 1 + n] = nums
        self.mx_cnt = [1] * (k * 2 - 1)

        for i in range(k - 2, -1, -1):
            if self.mx_tree[i * 2 + 1] > self.mx_tree[i * 2 + 2]:
                self.mx_tree[i] = self.mx_tree[i * 2 + 1]
                self.mx_cnt[i] = self.mx_cnt[i * 2 + 1]
            elif self.mx_tree[i * 2 + 1] < self.mx_tree[i * 2 + 2]:
                self.mx_tree[i] = self.mx_tree[i * 2 + 2]
                self.mx_cnt[i] = self.mx_cnt[i * 2 + 2]
            else:
                self.mx_tree[i] = self.mx_tree[i * 2 + 1]
                self.mx_cnt[i] = self.mx_cnt[i * 2 + 1] + self.mx_cnt[i * 2 + 2]

    def get_mx_and_its_cnt(self, l, r):
        cur_l = 0
        cur_r = (len(self.mx_tree) + 1) // 2
        return self.traversal(0, l, r, cur_l, cur_r)

    def traversal(self, i, l, r, cur_l, cur_r):
        if l <= cur_l and cur_r <= r:
            return self.mx_tree[i], self.mx_cnt[i]
        elif cur_l >= r or cur_r <= l:
            return float("-inf"), 0
        mx_left, cnt_left = self.traversal(i * 2 + 1, l, r, cur_l, (cur_l + cur_r) // 2)
        mx_right, cnt_right = self.traversal(i * 2 + 2, l, r, (cur_l + cur_r) // 2, cur_r)
        if mx_left > mx_right:
            return mx_left, cnt_left
        elif mx_left < mx_right:
            return mx_right, cnt_right
        else:
            return mx_left, cnt_left + cnt_right


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    k = int(input())
    for _ in range(k):
        l, r = map(int, input().split())
        print(*tree.get_mx_and_its_cnt(l - 1, r))


if __name__ == "__main__":
    main()
