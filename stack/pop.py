stack = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

if len(stack) == 0:
    print("stack Underflow")
else:
    removed = stack.pop()
    print("popped element:", stack)

print("stack value after pop:", stack)