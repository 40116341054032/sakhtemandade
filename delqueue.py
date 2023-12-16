class Queue:
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.front = -1
        self.rear = -1
    def delqueue(self):
        if (self.front == -1):
            print('empty')
        elif(self.front == self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return t
        else:
            t = self.queue[self.front]
            self.front += 1
            return t
    