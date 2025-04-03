class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, num):
        i = len(self.heap)
        self.heap.append(num)
        while i and self.heap[i] < self.heap[(parent := (i - 1) // 2)]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def extract(self):
        res = self.heap[0]

        self.heap[0] = self.heap[-1]
        i = 0
        n = len(self.heap)
        while i * 2 + 2 < n:
            mn = left if self.heap[(left := i * 2 + 1)] < self.heap[(right := i * 2 + 2)] else right
            if self.heap[mn] < self.heap[i]:
                self.heap[i], self.heap[mn] = self.heap[mn], self.heap[i]
                i = mn
            else:
                break

        self.heap.pop()

        return res


def main():
    n = int(input())
    h = Heap()
    for _ in range(n):
        op = list(map(int, input().split()))
        if len(op) == 1:
            print(-h.extract())
            # with open("out.txt", "a") as file:
            #     file.write(str(-h.extract()) + "\n")
        else:
            h.insert(-op[1])


if __name__ == "__main__":
    main()