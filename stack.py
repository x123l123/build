class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def empty(self):
        return self.items==[]
    def pop(self):
        if self.empty():
            return None
        else:
            return self.items.pop()
    def print_stack(self):
        print(self.items)
    def top(self):
        if self.empty():
            return None
        else:
            return self.items[-1]




stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print_stack()
stack.pop()
stack.print_stack()
print(stack.top())