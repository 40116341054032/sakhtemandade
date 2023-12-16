def delqueue_c():
    if (front == -1):
        print('empty')
    elif(front == rear):
        t = queue[front]
        front = -1
        rear = -1
        return t
    else:
        t = queue[front]
        front = (front + 1) % k 
        return t