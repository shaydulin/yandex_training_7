class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def ADD(self, num):
        num = int(num)

        if self.root is None:
            self.root = TreeNode(num)
            res = "DONE"
        else:
            root = self.root
            res = None
            while res is None:
                if num == root.val:
                    res = "ALREADY"
                elif num < root.val:
                    if root.left is None:
                        root.left = TreeNode(num)
                        res = "DONE"
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        root.right = TreeNode(num)
                        res = "DONE"
                    else:
                        root = root.right
        print(res)

    def SEARCH(self, num):
        num = int(num)

        root = self.root
        res = None
        while res is None:
            if root is None:
                res = "NO"
            elif root.val == num:
                res = "YES"
            elif root.val > num:
                root = root.left
            else:
                root = root.right
        print(res)

    def PRINTTREE(self):
        self.print_node(self.root, 0)
    
    def print_node(self, node, lvl):
        if node.left:
            self.print_node(node.left, lvl + 1)
        print("." * lvl + str(node.val))
        if node.right:
            self.print_node(node.right, lvl + 1)


def main():
    binary_tree = BinaryTree()

    with open("input.txt") as file:
        while (query := file.readline().split()):
            getattr(binary_tree, query[0])(*query[1:])

if __name__ == "__main__":
    main()