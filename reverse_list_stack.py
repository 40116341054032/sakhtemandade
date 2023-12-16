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

def reverse(lst):
    s = stack()
    for e in lst:
        s.push(e)
    for i in range(len(lst)):
        lst[i] = s.pop()