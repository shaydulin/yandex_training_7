# v2

def create_node(left_bound, right_bound):
    return [
        0, # cnt - 0
        0, # square_sum - 1
        None, # left - 2
        None, # right - 3
        None if left_bound != right_bound else right_bound, # first - 4
        None if left_bound != right_bound else right_bound, # last - 5
        False # to_remove - 6
    ]


class SegmentTree:
    def __init__(self, arr: list):
        self.right_bound = sum(arr)
        self.root = create_node(0, self.right_bound)
        arr.append(None)
        it = iter(arr)
        self.build(self.root, it, 0, 0, self.right_bound)
        arr.pop()
        # self.print_tree(self.root, 1, 0, self.right_bound)

    def build(self, root, it, cur_val, left_bound, right_bound):
        # base case, we are in needed node
        if right_bound == left_bound:
            nxt_val = next(it)
            return cur_val + nxt_val if nxt_val is not None else None

        middle = (left_bound + right_bound) >> 1
        while cur_val is not None and cur_val <= right_bound:
            if cur_val <= middle:
                if root[2] is None:
                    root[2] = create_node(left_bound, middle)
                cur_val = self.build(root[2], it, cur_val, left_bound, middle)
            else:
                if root[3] is None:
                    root[3] = create_node(middle + 1, right_bound)
                cur_val = self.build(root[3], it, cur_val, middle + 1, right_bound)
        self.update(root)

        return cur_val

    def divide_and_join(self, v):
        left_border, middle, right_border = self.traversal(v, self.root, True)
        if left_border != 0 and right_border != self.right_bound:
            self.add(self.root, middle, 0, self.right_bound)
        if left_border != 0:
            self.remove(self.root, left_border, 0, self.right_bound)
        if right_border != self.right_bound:
            self.remove(self.root, right_border, 0, self.right_bound)
        return self.root[1]

    def divide(self, v):
        left_border, middle, right_border = self.traversal(v, self.root, False)
        self.add(self.root, middle, 0, self.right_bound)
        return self.root[1]

    def traversal(self, v, root, remove_nodes):
        cnt_l = root[2][0] if root[2] else 0
        cnt_r = root[3][0] if root[3] else 0
        if cnt_l >= v:
            return self.traversal(v, root[2], remove_nodes)
        elif cnt_l == v - 1 and root[0] - cnt_l - cnt_r != 0:
            return root[2][5], (root[3][4] + root[2][5]) >> 1, root[3][4]
        else:
            v -= cnt_l
            if root[0] - cnt_l - cnt_r != 0:
                v -= 1
            return self.traversal(v, root[3], remove_nodes)

    def remove(self, root, border, left_bound, right_bound):
        middle = (left_bound + right_bound) >> 1
        if border <= middle:
            if middle - left_bound > 0:
                self.remove(root[2], border, left_bound, middle)
                if root[2][6]:
                    node = root[2]
                    root[2] = None
                    del node
            else:
                node = root[2]
                root[2] = None
                del node
        else:
            if right_bound - middle - 1 > 0:
                self.remove(root[3], border, middle + 1, right_bound)
                if root[3][6]:
                    node = root[3]
                    root[3] = None
                    del node
            else:
                node = root[3]
                root[3] = None
                del node
        if root[2] is None and root[3] is None:
            root[6] = True
        else:
            self.update(root)

    def add(self, root, border, left_bound, right_bound):
        middle = (left_bound + right_bound) >> 1
        if border <= middle:
            if root[2] is None:
                root[2] = create_node(left_bound, middle)
            if middle - left_bound > 0:
                self.add(root[2], border, left_bound, middle)
        else:
            if root[3] is None:
                root[3] = create_node(middle + 1, right_bound)
            if right_bound - middle - 1 > 0:
                self.add(root[3], border, middle + 1, right_bound)
        self.update(root)

    def update(self, root):
        l = root[2]
        r = root[3]
        last_left = first_right = None
        root[0] = 0
        root[1] = 0
        if l is not None:
            root[0] += l[0]
            root[1] += l[1]
            root[4] = l[4]
            last_left = l[5]
            if r is None:
                root[5] = l[5]
        if r is not None:
            root[0] += r[0]
            root[1] += r[1]
            root[5] = r[5]
            first_right = r[4]
            if l is None:
                root[4] = r[4]
        if last_left is not None and first_right is not None:
            root[0] += 1
            root[1] += (first_right - last_left)**2

    def print_tree(self, root, lvl, left_bound, right_bound):
        print(
            "." * lvl,
            f"{left_bound} - {right_bound} |",

            f"cnt: {root[0]} |",
            f"sq: {root[1]}",
            f"first: {root[4]} last: {root[5]} |",
        )
        if root[2]:
            self.print_tree(root[2], lvl + 1, left_bound, (left_bound + right_bound) >> 1)
        if root[3]:
            self.print_tree(root[3], lvl + 1, ((left_bound + right_bound) >> 1) + 1, right_bound)


with open("input.txt") as file:
    n = int(file.readline())
    a = list(map(int, file.readline().split()))
    tree = SegmentTree(a)
    del a

    ans = [tree.root[1]]

    k = int(file.readline())
    for i in range(3, 3 + k):
        typ, v = map(int, file.readline().split())
        if typ == 1:
            ans.append(tree.divide_and_join(v))
        else:
            ans.append(tree.divide(v))
    print("\n".join(map(str, ans)))


# v1
class TreeNode:
    def __init__(self, left_bound, right_bound):
        self.left_bound = left_bound
        self.right_bound = right_bound

        self.cnt = 0
        self.square_sum = 0

        self.left = None
        self.first = None if left_bound != right_bound else right_bound

        self.right = None
        self.last = None if left_bound != right_bound else right_bound

        self.to_remove = False


class SegmentTree:
    def __init__(self, arr: list):
        sm = sum(arr)
        self.root = TreeNode(0, sm)
        arr.append(None)
        it = iter(arr)
        self.build(self.root, it, 0)
        arr.pop()
        # self.print_tree(self.root, 1)

    def build(self, root: TreeNode, it, cur_val):
        # base case, we are in needed node
        if root.right_bound == root.left_bound:
            nxt_val = next(it)
            return cur_val + nxt_val if nxt_val is not None else None

        middle = (root.left_bound + root.right_bound) // 2
        while cur_val is not None and cur_val <= root.right_bound:
            if cur_val <= middle:
                if root.left is None:
                    root.left = TreeNode(root.left_bound, middle)
                cur_val = self.build(root.left, it, cur_val)
            else:
                if root.right is None:
                    root.right = TreeNode(middle + 1, root.right_bound)
                cur_val = self.build(root.right, it, cur_val)
        self.update(root)

        return cur_val

    def divide_and_join(self, v):
        left_border, middle, right_border = self.traversal(v, self.root, True)
        if left_border != 0 and right_border != self.root.right_bound:
            self.add(self.root, middle)
        if left_border != 0:
            self.remove(self.root, left_border)
        if right_border != self.root.right_bound:
            self.remove(self.root, right_border)
        return self.root.square_sum

    def divide(self, v):
        left_border, middle, right_border = self.traversal(v, self.root, False)
        self.add(self.root, middle)
        return self.root.square_sum

    def traversal(self, v, root: TreeNode, remove_nodes: bool):
        cnt_l = root.left.cnt if root.left else 0
        cnt_r = root.right.cnt if root.right else 0
        if cnt_l >= v:
            return self.traversal(v, root.left, remove_nodes)
        elif cnt_l == v - 1 and root.cnt - cnt_l - cnt_r != 0:
            left_border = root.left.last
            right_border = root.right.first
            middle = (right_border + left_border) // 2
            return left_border, middle, right_border
        else:
            v -= cnt_l
            if root.cnt - cnt_l - cnt_r != 0:
                v -= 1
            return self.traversal(v, root.right, remove_nodes)

    def remove(self, root: TreeNode, border):
        middle = (root.left_bound + root.right_bound) // 2
        if border <= middle:
            if middle - root.left_bound > 0:
                self.remove(root.left, border)
                if root.left.to_remove:
                    root.left = None
            else:
                root.left = None
        else:
            if root.right_bound - middle - 1 > 0:
                self.remove(root.right, border)
                if root.right.to_remove:
                    root.right = None
            else:
                root.right = None
        if root.left is None and root.right is None:
            root.to_remove = True
        else:
            self.update(root)

    def add(self, root: TreeNode, v):
        middle = (root.left_bound + root.right_bound) // 2
        if v <= middle:
            if root.left is None:
                root.left = TreeNode(root.left_bound, middle)
            if middle - root.left_bound > 0:
                self.add(root.left, v)
        else:
            if root.right is None:
                root.right = TreeNode(middle + 1, root.right_bound)
            if root.right_bound - middle - 1 > 0:
                self.add(root.right, v)
        self.update(root)

    def update(self, root: TreeNode):
        l: TreeNode = root.left
        r: TreeNode = root.right
        last_left = first_right = None
        root.cnt = 0
        root.square_sum = 0
        if l is not None:
            root.cnt += l.cnt
            root.square_sum += l.square_sum
            root.first = l.first
            last_left = l.last
            if r is None:
                root.last = l.last
        if r is not None:
            root.cnt += r.cnt
            root.square_sum += r.square_sum
            root.last = r.last
            first_right = r.first
            if l is None:
                root.first = r.first
        if last_left is not None and first_right is not None:
            root.cnt += 1
            root.square_sum += (first_right - last_left)**2

    def print_tree(self, root: TreeNode, lvl):
        print(
            "." * lvl,
            f"{root.left_bound} - {root.right_bound} |",

            f"cnt: {root.cnt} |",
            f"sq: {root.square_sum}",
            f"first: {root.first} last: {root.last} |",
        )
        if root.left:
            self.print_tree(root.left, lvl + 1)
        if root.right:
            self.print_tree(root.right, lvl + 1)

def main():
    data = open("input.txt").readlines()

    n = int(data[0])
    a = list(map(int, data[1].split()))

    tree = SegmentTree(a)
    ans = [tree.root.square_sum]

    k = int(data[2])
    for idx, i in enumerate(range(3, 3 + k), 1):
        if idx == 77:
            pass
        typ, v = map(int, data[i].split())
        if typ == 1:
            ans.append(tree.divide_and_join(v))
        else:
            ans.append(tree.divide(v))
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
