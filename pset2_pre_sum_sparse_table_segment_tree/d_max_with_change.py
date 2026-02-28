from itertools import count


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)
        self.mx_tree = [float("-inf")] * (k * 2 - 1)
        self.start = k - 1
        self.mx_tree[self.start:self.start + n] = nums

        for i in range(k - 2, -1, -1):
            self.mx_tree[i] = max(self.mx_tree[i * 2 + 1], self.mx_tree[i * 2 + 2])

    def update_element(self, i, val):
        i += self.start
        self.mx_tree[i] = val
        while (parent := (i - 1) // 2) >= 0:
            self.mx_tree[parent] = max(self.mx_tree[parent * 2 + 1], self.mx_tree[parent * 2 + 2])
            i = parent

    def get_mx(self, l, r):
        return self.traversal(0, l, r, 0, (len(self.mx_tree) + 1) // 2)

    def traversal(self, i, l, r, cur_l, cur_r):
        if l <= cur_l and cur_r <= r:
            return self.mx_tree[i]
        elif cur_l >= r or cur_r <= l:
            return float("-inf")
        mx_left = self.traversal(i * 2 + 1, l, r, cur_l, (cur_l + cur_r) // 2)
        mx_right = self.traversal(i * 2 + 2, l, r, (cur_l + cur_r) // 2, cur_r)
        return mx_left if mx_left > mx_right else mx_right


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
            ans.append(tree.get_mx(int(q[1]) - 1, int(q[2])))
    print(*ans)


if __name__ == "__main__":
    main()
