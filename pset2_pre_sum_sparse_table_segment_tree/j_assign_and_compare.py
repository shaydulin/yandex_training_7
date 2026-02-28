from itertools import count
import sys


class SegmentTree:
    def __init__(self, n, nums):
        k = next(1 << i for i in count() if 1 << i >= n)

        self.M = 1_000_000_007
        self.X = 101_113
        self.x = [1] * (n + 1)
        self.h = [0] * (n + 1)
        for i in range(1, n + 1):
            self.x[i] = self.x[i - 1] * self.X % self.M
            self.h[i] = (self.h[i - 1] + self.x[i - 1]) % self.M

        self.val_tree = [0] * (k * 2 - 1)
        self.val_tree[k - 1:k - 1 + n] = nums
        self.hash_tree = self.val_tree.copy()
        self.length_tree = [0] * (k - 1) + [1] * k

        for i in range(k - 2, -1, -1):
            cur_length = self.length_tree[i * 2 + 1]
            self.length_tree[i] = cur_length * 2
            self.hash_tree[i] = (self.hash_tree[i * 2 + 1] * self.x[cur_length] + self.hash_tree[i * 2 + 2]) % self.M

    def assign(self, l, r, val):
        self.traversal(0, l, r, val, 0, (len(self.val_tree) + 1) // 2)

    def compare(self, l1, l2, length):
        _, hash_l = self.traversal(0, l1, l1 + length, 0, 0, (len(self.val_tree) + 1) // 2)
        _, hash_r = self.traversal(0, l2, l2 + length, 0, 0, (len(self.val_tree) + 1) // 2)
        return hash_l == hash_r

    def traversal(self, i, l, r, val, cur_l, cur_r):
        # return len, hash
        if cur_l >= r or cur_r <= l:
            if self.val_tree[i]:
                self.hash_tree[i] = (self.val_tree[i] * self.h[self.length_tree[i]]) % self.M
            return 0, self.hash_tree[i]

        if l <= cur_l and cur_r <= r:
            if val:
                self.val_tree[i] = val
            if self.val_tree[i]:
                self.hash_tree[i] = (self.val_tree[i] * self.h[self.length_tree[i]]) % self.M
            return self.length_tree[i], self.hash_tree[i]

        if self.val_tree[i]:
            self.val_tree[i * 2 + 1] = self.val_tree[i]
            self.val_tree[i * 2 + 2] = self.val_tree[i]
            self.val_tree[i] = 0
        length_l, hash_l = self.traversal(i * 2 + 1, l, r, val, cur_l, (cur_l + cur_r) // 2)
        length_r, hash_r = self.traversal(i * 2 + 2, l, r, val, (cur_l + cur_r) // 2, cur_r)
        child_length = self.length_tree[i] // 2
        self.hash_tree[i] = (self.hash_tree[i * 2 + 1] * self.x[child_length] + self.hash_tree[i * 2 + 2]) % self.M
        return (
            length_l + length_r,
            (hash_l * self.x[length_r] * int(length_l != 0) + hash_r * int(length_r != 0)) % self.M,
        )


def main():
    data = sys.stdin.read().splitlines()
    
    n = int(data[0])
    nums = list(map(int, data[1].split()))
    tree = SegmentTree(n, nums)
    
    m = int(data[2])
    ans = []
    
    for i in range(3, 3 + m):
        t, l, r, k = map(int, data[i].split())
        if t == 0:
            tree.assign(l - 1, r, k)
        else:
            if l == r:
                ans.append("+")
            else:
                ans.append("+" if tree.compare(l - 1, r - 1, k) else "-")
    
    sys.stdout.write("".join(ans))


if __name__ == "__main__":
    main()
