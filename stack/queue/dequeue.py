queue = [10, 20, 30, 40]

if len(queue) == 0:
    print("Quese underflow! cannot dequeue")

else:
    removed = queue.pop(0)
    print("dequeue element: ", removed)

print("Queue after dequese:", queue)