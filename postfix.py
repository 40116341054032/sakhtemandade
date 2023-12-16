class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def peek(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    def push(self, data):
        if len(self.stack) >= self.limit:
            return -1
        else:
            self.stack.append(data)  # Corrected the typo, should be 'append' not 'appned'

    @staticmethod
    def repost(lst):
        s = Stack(len(lst) // 2)  # Corrected the typo, should be 'Stack' not 'stack'
        for e in lst:
            if e == '*':
                t2 = s.pop()
                t1 = s.pop()
                t = t1 * t2
                s.push(t)
            elif e in ('+', '/', '-', '//'):  # Corrected the condition
                t2 = s.pop()
                t1 = s.pop()
                if e == '+':
                    t = t1 + t2
                elif e == '/':
                    t = t1 / t2
                elif e == '-':
                    t = t1 - t2
                elif e == '//':
                    t = t1 // t2
                s.push(t)
            else:
                s.push(e)
        return s.pop()  # Return the top element, not the entire stack[0]

