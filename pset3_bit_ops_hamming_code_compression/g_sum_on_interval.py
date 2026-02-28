from itertools import accumulate


class FenwickTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.fenwick = [*accumulate(nums)]
        for i in range(len(nums) - 1, -1, -1):
            j = i & i + 1
            if not j:
                continue
            self.fenwick[i] -= self.fenwick[j - 1]

    def get_sum_on_interval(self, l, r):
        return self.get_prefix_sum(r) - self.get_prefix_sum(l - 1)

    def get_prefix_sum(self, i):
        res = 0
        while i != -1:
            res += self.fenwick[i]
            i = (i & i + 1) - 1
        return res

    def assign(self, i, val):
        self.add_to_element(i, val - self.nums[i])
        self.nums[i] = val

    def add_to_element(self, i, val):
        while i < self.n:
            self.fenwick[i] += val
            i |= i + 1


def main():
    n, k = map(int, input().split())
    fw = FenwickTree([0] * n)
    ans = []
    for _ in range(k):
        query = input().split()
        if query[0] == "A":
            fw.assign(int(query[1]) - 1, int(query[2]))
        else:
            ans.append(fw.get_sum_on_interval(int(query[1]) - 1, int(query[2]) - 1))
    print("\n".join(map(str, ans)))


def draw(n):
    for i in range(n):
        j = i & i + 1
        print(str(i).rjust(2), " " * 2, bin(i)[2:].rjust(5, "0"), " " * 2, " ".join("." * j + "#" * (i - j + 1)), " " * 2, i - j + 1)


if __name__ == "__main__":
    main()
    # draw(32)
