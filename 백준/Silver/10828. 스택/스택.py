import sys

class Stack:
    inner = []

    def __init__(self):
        pass

    def push(self, x):
        self.inner.append(x)

    def pop(self):
        if len(self.inner) > 0:
            print(self.inner.pop())
        else:
            print(-1)

    def top(self):
        if len(self.inner) > 0:
            print(self.inner[-1])
        else:
            print(-1)

    def empty(self):
        if len(self.inner) == 0:
            print(1)
        else:
            print(0)

    def size(self):
        print(len(self.inner))


n = int(sys.stdin.readline())
stack = Stack()

for _ in range(n):
    lst = list(sys.stdin.readline().split())

    if lst[0] == 'push':
        stack.push(lst[1])
    if lst[0] == 'top':
        stack.top()
    if lst[0] == 'size':
        stack.size()
    if lst[0] == 'empty':
        stack.empty()
    if lst[0] == 'pop':
        stack.pop()
