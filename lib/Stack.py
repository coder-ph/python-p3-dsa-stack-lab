class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) ==0
      

    def push(self, item):
        if self.full():
        
            raise OverflowError("stack is full")
        else:
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()
        
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def size(self):
       return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return len(self.items) -1 - self.items.index(target)
        return -1
