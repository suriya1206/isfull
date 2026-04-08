class queue:

    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, value):
        if len(self.queue) == self.size:
            print("queue Overflow")
        else:
            self.queue.append(value)
            print(value, "Enqueded")

    def dequeue(self):
        if len(self.queue) == 0:
            print("queue Underflow")
        else:
            print(self.queue.pop(),"Dequeued")
           
    def front(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            print("Top:", self.queue[-1])

    def rear(self):
        return len(self.queue) == self.size
    
    def isempty(self):
        return len(self.queue) == 0
    
    def display(self):
        print("Queue: ", self.queue)

a = queue(3)
while True:
    print("Menu queue")
    print("1 : Enqueue")
    print("2 : Dequeue")
    print("3 : front")
    print("4 : rear")
    print("5 : isempty")
    print("6 : display")
    print("7 : Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = input("Enter value to Enqueue: ")
        a.enqueue(n)
    elif choice == 2:
        a.dequeue()
    elif choice == 3:
        a.front()
    elif choice == 4:
        print("Rear:", a.rear())
    elif choice == 5:
        print("Is empty:", a.isempty())
    elif choice == 6:
        a.display()
    elif choice == 7:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")