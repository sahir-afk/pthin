
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
for letter in "Uzbekistan":
    stack.push(letter)

reverse = ""

for i in range(len(stack.data)):
    reverse += stack.pop()

print(reverse)

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