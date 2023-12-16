class Queue:
    def __init__(self,k):
        self.k = k
        self.queue = [None]*k
        self.front = -1
        self.rear = -1
    def insqueue(self,data):
        if (self.rear == -1):
            self.front = 0
            self.rear = 0
            self.queue[0] = data
        elif(self.rear+1 == self.k):
            print('is full')
            return
        else:
            self.rear += 1
            self.queue[self.rear] = data
