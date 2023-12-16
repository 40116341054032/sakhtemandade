class stack():
    def __init__(self,limit = 10):
        self.stack = []
        self.limit == limit
    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack)-1]
        
    def is_empty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False 
    
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

    
    def dec2bin(number):
        s = stack()
        while number > 0:
            r = number % 2
            s.push(r)
            number = number//2
        b = " "
        while not s.is_empty():
            b = b+str(s.pop())
        return b