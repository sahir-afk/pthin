
# LIFO
class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
    
    def is_empty(self):
        return self.data == []
    
    def pop(self):
        return self.data.pop()
    
    def peek(self):
        last = len(self.data) - 1
        return self.data[last]
    
    def size(self):
        return len(self.data)
    
stack = Stack()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    stack.push(num)
for i in range(stack.size()):
    print(stack.pop())

#FIFO
class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, val):
        self.items.insert(0, val)
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
q = queue()
for i in range(0, 7):
    q.enqueue(i)

print(q.dequeue())

