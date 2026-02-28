class ListNode:
    def __init__(self, length, left=None, right=None):
        self.length: int = length
        self.left: ListNode = left
        self.right: ListNode = right


def main():
    with open("input.txt") as file:
        n = int(file.readline())
        ans = [0]
        cur = prev = ListNode(0)
        for length in map(int, file.readline().split()):
            ans[0] += length**2
            prev.right = ListNode(length, prev)
            prev = prev.right

        cur: ListNode = cur.right
        cur.left = None
        cur_pos = 1

        k = int(file.readline())
        for _ in range(3, 3 + k):
            typ, v = map(int, file.readline().split())
            while cur_pos < v:
                cur = cur.right
                cur_pos += 1
            while cur_pos > v:
                cur = cur.left
                cur_pos -= 1

            res = ans[-1] - cur.length**2
            if typ == 1:
                if cur.left is None:
                    res -= cur.right.length**2
                    cur.right.length += cur.length
                    cur = cur.right
                    cur.left = None
                    res += cur.length**2
                elif cur.right is None:
                    res -= cur.left.length**2
                    cur.left.length += cur.length
                    cur = cur.left
                    cur.right = None
                    res += cur.length**2
                    cur_pos -= 1
                else:
                    length_left = cur.length >> 1
                    length_right = cur.length - length_left
                    res -= cur.left.length**2
                    cur.left.length += length_left
                    res += cur.left.length**2
                    res -= cur.right.length**2
                    cur.right.length += length_right
                    res += cur.right.length**2
                    cur = cur.right
                    cur.left = cur.left.left
                    cur.left.right = cur
            else:
                length_left = cur.length >> 1
                length_right = cur.length - length_left
                res += length_left**2 + length_right**2
                cur.length = length_right
                cur.left = ListNode(length_left, cur.left, cur)
                cur = cur.left
                if cur.left is not None:
                    cur.left.right = cur
            ans.append(res)
        print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()


