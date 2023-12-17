class clinkedlist:
    def __init__(self):
        self.head = None
    def delete(self,data):
        if self.head == None:
            print('empty')
            return
        if self.head.next == self.head:
            if self.head.data == data:
                self.head = None
                return
            return -1
        t = self.head
        while (t.data != data):
            p = t
            t = t.next
            if t == self.head:
                return -1
        p.next = t.next
        t.next = None
