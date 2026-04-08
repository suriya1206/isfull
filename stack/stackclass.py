class stack:

    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) == self.size:
            print("stack overflow")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
            
        else:
            print(self.stack.pop(), "popped")

    def peek(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print("top:", self.stack[-1])

    def isfull(self):
        return len(self.stack) == self.size
    def isempty(self):
        return len(self.stack) == 0
    def display(self):
        print("self:", self.stack)

a = stack(3)

a.push(10)
a.push(20)
a.push(30)
a.push(40)

a.display()

a.pop()
a.peek()

print("Empty?", a.isempty())
print("Full?", a.isfull())