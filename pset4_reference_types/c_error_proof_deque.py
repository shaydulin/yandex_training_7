import sys


class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev: Node = prev
        self.next: Node = next


def main():
    head = tail = None
    size = 0

    for chunk in map(str.split, open(0).readlines()):
        match chunk[0]:
            case "push_front":
                if head is None:
                    head = tail = Node(chunk[1])
                else:
                    head.prev = Node(chunk[1], next=head)
                    head = head.prev
                size += 1
                print("ok")
            case "push_back":
                if tail is None:
                    head = tail = Node(chunk[1])
                else:
                    tail.next = Node(chunk[1], prev=tail)
                    tail = tail.next
                size += 1
                print("ok")
            case "pop_front":
                if head is None:
                    print("error")
                else:
                    print(head.val)
                    head = head.next
                    if head is None:
                        tail = None
                    else:
                        head.prev = None
                    size -= 1
            case "pop_back":
                if tail is None:
                    print("error")
                else:
                    print(tail.val)
                    tail = tail.prev
                    if tail is None:
                        head = None
                    else:
                        tail.next = None
                    size -= 1
            case "front":
                print(head.val if head is not None else "error")
            case "back":
                print(tail.val if tail is not None else "error")
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
