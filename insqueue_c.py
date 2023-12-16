def insqueue_c(self,data):
    if ((rear + 1) % k == front):
        print('full')
    elif(front == 1):
        fornt = 0
        rear = 0
        queue[rear] = data
    else:
        rear = (rear + 1) % k
        queue[rear] = data
