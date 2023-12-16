class Queue:
    def __init__(self , k):
        self.k = k
        self.queue = [None]*k
        self.front = -1
        self.rear = -1
    def disqueue(self):
        if (self.front == -1):
            print('empty')
        for i in range(self.front , self.rear+1):
            print(self.queue[i])
     
    