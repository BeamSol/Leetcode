# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        inst = input().split()
        cmd = inst[0]

        if cmd == "print":
            print(arr)

        elif cmd == "sort":
            arr.sort()

        elif cmd == "pop":
            arr.pop()

        elif cmd == "reverse":
            arr.reverse()

        elif cmd == "insert":
            index = int(inst[1])
            value = int(inst[2])
            arr.insert(index, value)

        elif cmd == "append":
            value = int(inst[1])
            arr.append(value)

        elif cmd == "remove":
            value = int(inst[1])
            arr.remove(value)
