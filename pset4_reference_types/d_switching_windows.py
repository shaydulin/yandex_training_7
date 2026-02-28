class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev: Node = prev
        self.next: Node = next


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        self.head = Node(val, self.head)
        if self.head.prev is not None:
            self.head.prev.next = self.head
        self.size += 1

    def switch(self, n):
        if not self.size:
            return

        tmp = self.head
        for _ in range(n % self.size):
            tmp = tmp.prev

        if tmp is self.head:
            return

        tmp.next.prev = tmp.prev
        if tmp.prev is not None:
            tmp.prev.next = tmp.next
        tmp.prev = self.head
        tmp.next = None
        self.head.next = tmp
        self.head = tmp


def main():
    windows = Queue()

    n = int(input())

    for _ in range(n):
        q = input()
        if q.startswith("Run"):
            if len(q) == 3:
                print()
                continue
            windows.push(q.split(maxsplit=1)[1])
        else:
            windows.switch(q.count("+"))
        print(windows.head.val if windows.head else "")


if __name__ == "__main__":
    main()
