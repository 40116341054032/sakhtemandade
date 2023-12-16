class Queue_c:
    def __init__(self , k):
        self.k = k
        self.queue = [None]*k
        self.front = -1
        self.rear = -1
        