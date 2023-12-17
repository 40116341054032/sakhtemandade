class linkedlist:
    def __init__(self):
        self.head = None
    
    def dellast(self):
        t = self.head
        if (t == None):
            return True
        elif (t.next == None):
            t == None
        while (t.next.next != None):
            t = t.next
        t.next = None