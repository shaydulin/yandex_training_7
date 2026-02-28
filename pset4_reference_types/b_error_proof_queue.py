import sys


class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next: Node = next
        self.prev: Node = prev


def main():
    head = tail = None
    size = 0

    for chunk in map(str.split, open(0).readlines()):
        match chunk[0]:
            case "push":
                if head is None:
                    head = tail = Node(chunk[1])
                else:
                    tail.prev = Node(chunk[1], tail)
                    tail = tail.prev
                size += 1
                print("ok")
            case "pop":
                if head is None:
                    print("error")
                else:
                    print(head.val)
                    head = head.prev
                    if head is not None:
                        head.next = None
                    size -= 1
            case "front":
                print(head.val if head is not None else "error")
            case "size":
                print(size)
            case "clear":
                head = tail = None
                size = 0
                print("ok")
            case "exit":
                print("bye")
                sys.exit()


if __name__ == "__main__":
    main()
