class stack:

    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, value):
        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(value)
            print(value, "pushed")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(),"Popped")
           
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top:", self.stack[-1])

    def isfull(self):
        return len(self.stack) == self.size
    
    def isempty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("Stack: ", self.stack)

a = stack(3)
while True:
    print("Menu stack")
    print("1 : push")
    print("2 : pop")
    print("3 : peek")
    print("4 : isfull")
    print("5 : isempty")
    print("6 : display")
    print("7 : Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = input("Enter value to push: ")
        a.push(n)
    elif choice == 2:
        a.pop()
    elif choice == 3:
        a.peek()
    elif choice == 4:
        print("Is full:", a.isfull())
    elif choice == 5:
        print("Is empty:", a.isempty())
    elif choice == 6:
        a.display()
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")