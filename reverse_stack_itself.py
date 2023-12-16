class stack():
    def __init__(self,limit = 10):
        self.stack = []
        self.limit == limit
    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack)-1]
        

    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()
    
    def push(self,data):
        if len(self.stack) >= self.limit:
            return -1
        else:
            self.stack.appned(data)


    def reverse_stack(s):
        s1 = stack()
        s2 = stack()
        while not s.is_empty():
         s1.push(s.pop())
        while not s1.is_empty():
            s2.push(s1.pop())
        while not s2.is_empty():
            s.push(s2.pop())