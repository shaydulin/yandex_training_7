import sys


def main():
    stack = []
    data = open(0).readlines()

    for chunk in map(str.split, data):
        match chunk[0]:
            case "push":
                stack.append(chunk[1])
                print("ok")
            case "pop":
                print(stack.pop() if stack else "error")
            case "back":
                print(stack[-1] if stack else "error")
            case "size":
                print(stack.__len__())
            case "clear":
                stack.clear()
                print("ok")
            case "exit":
                print("bye")
                sys.exit()


if __name__ == "__main__":
    main()
