class Stacks:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
    
    def is_empty(self):
        return self.data == []
    
    def pop(self):
        self.data.pop()
    
    def peek(self):
        last = len(self.data - 1)
        return self.data[last]
    
    def size(self):
        return len(self.data)