class linkedlist:
    def __init__(self):
        self.head = None
        
    def delafter(self,m):
        t = self.head
        while (t.data != m):
            t = t.next
        t.next = t.next.next