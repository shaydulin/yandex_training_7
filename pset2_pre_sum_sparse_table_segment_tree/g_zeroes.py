from itertools import count
import array
import copy


class SegmentTree:
    def __init__(self, n, nums):
        self.nums = nums
        k = next(1 << i for i in count() if 1 << i >= n)
        self.zero_idx = k - 1
        self.zero_cnt = array.array("i", [0] * (k * 2 - 1))
        self.zero_cnt[self.zero_idx:self.zero_idx + n] = array.array("i", (int(num == 0) for num in nums))
        self.zero_pre = copy.copy(self.zero_cnt)
        self.zero_suf = copy.copy(self.zero_cnt)
        self.segment_is_zero = copy.copy(self.zero_cnt)

        for i in range(k - 2, -1, -1):
            self.calc_for_idx(i)

    def update_element(self, i, val):
        tmp = self.nums[i]
        self.nums[i] = val
        if val and tmp:
            return
        i += self.zero_idx
        self.zero_cnt[i] = self.zero_pre[i] = self.zero_suf[i] = self.segment_is_zero[i] = int(val == 0)
        while (i := (i - 1) // 2) >= 0:
            self.calc_for_idx(i)

    def calc_for_idx(self, i):
        l, r = i * 2 + 1, i * 2 + 2
        self.zero_cnt[i] = max(
            self.zero_cnt[l],
            self.zero_cnt[r],
            self.zero_suf[l] + self.zero_pre[r],
        )
        self.zero_pre[i] = self.zero_pre[l] + self.zero_pre[r] if self.segment_is_zero[l] else self.zero_pre[l]
        self.zero_suf[i] = self.zero_suf[l] + self.zero_suf[r] if self.segment_is_zero[r] else self.zero_suf[r]
        self.segment_is_zero[i] = self.segment_is_zero[l] & self.segment_is_zero[r]

    def get_contiguous_zero_count(self, l, r):
        return self.traversal(0, l, r, 0, (len(self.zero_cnt) + 1) // 2)[0]

    def traversal(self, i, l, r, cur_l, cur_r):
        if l <= cur_l and cur_r <= r:
            return (
                self.zero_cnt[i],
                self.zero_pre[i],
                self.zero_suf[i],
                self.segment_is_zero[i],
            )
        elif cur_l >= r or cur_r <= l:
            return 0, 0, 0, 0

        cnt_l, pre_l, suf_l, is_zero_l = self.traversal(i * 2 + 1, l, r, cur_l, (cur_l + cur_r) // 2)
        cnt_r, pre_r, suf_r, is_zero_r = self.traversal(i * 2 + 2, l, r, (cur_l + cur_r) // 2, cur_r)

        return (
            max(cnt_l, cnt_r, suf_l + pre_r),
            pre_l + pre_r if is_zero_l else pre_l,
            suf_l + suf_r if is_zero_r else suf_r,
            is_zero_l & is_zero_r,
        )


def main():
    n = int(input())

    nums = list(map(int, input().split()))
    tree = SegmentTree(n, nums)

    m = int(input())
    ans = []
    for _ in range(m):
        q = input().split()
        if q[0] == "UPDATE":
            tree.update_element(int(q[1]) - 1, int(q[2]))
        else:
            ans.append(tree.get_contiguous_zero_count(int(q[1]) - 1, int(q[2])))
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
