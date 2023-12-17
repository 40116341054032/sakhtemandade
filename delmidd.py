class dlinkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        t = self.head
        while (t != None):
            print(t.data , end = '<-->')
        print('None')

    def delmid(self):
        t = self.head
        count = 0
        while(t != None):
            t = t.next
            count += 1
        t = self.head
        if count % 2 == 0:
            for i in range(count // 2):
                t = t.next
        else:
            for i in range(count // 2):
                t = t.next
                t.next.prev = t.prev
                t.prev.next = t.next
                t.next = None
                t.prev = None