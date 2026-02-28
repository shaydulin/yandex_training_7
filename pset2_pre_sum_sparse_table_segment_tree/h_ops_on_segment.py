from itertools import count
import array


class SegmentTree:
    def __init__(self, n, nums):
        self.nums = nums
        k = next(1 << i for i in count() if 1 << i >= n)
        self.to_add = array.array("I", [0] * (k * 2 - 1))

    def get_item(self, idx):
        self.add_on_segment(idx, idx + 1, 0)
        return self.nums[idx]

    def add_on_segment(self, l, r, val):
        self.traversal(0, l, r, val, 0, len(self.nums))

    def traversal(self, i, l, r, val, cur_l, cur_r):
        if cur_l >= r or cur_r <= l:
            return

        if cur_r - cur_l == 1:
            self.nums[cur_l] += self.to_add[i] + val
            self.to_add[i] = 0
            return

        if l <= cur_l and cur_r <= r:
            self.to_add[i] += val
        else:
            self.to_add[i * 2 + 1] += self.to_add[i]
            self.to_add[i * 2 + 2] += self.to_add[i]
            self.to_add[i] = 0
            self.traversal(i * 2 + 1, l, r, val, cur_l, (cur_l + cur_r) // 2)
            self.traversal(i * 2 + 2, l, r, val, (cur_l + cur_r) // 2, cur_r)


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
            ans.append(tree.get_item(int(q[1]) - 1))
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
