class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def empty(self):
        if self.items:
            return 0
        else:
            return 1

    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")

        return self.items.pop()

    def top(self):
        if self.empty():
            return Exception("Stack is empty")
        return self.items[-1]


N = int(input())
stack = Stack()

for i in range(N):
    order = list(input().split())
    if order[0] == "push":
        stack.push(order[1])
    elif order[0] == "size":
        print(stack.size())
    elif order[0] == "empty":
        print(stack.empty())
    elif order[0] == "top":
        print(stack.top())
    else:
        print(stack.pop())
