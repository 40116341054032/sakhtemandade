class dnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
    def addinend(self,d):
        n = dnode(d)
        if self.head != None:
            t = self.head
            while(t.next != None):
                t = t.next
            t.next = n
            n.prev = t
        else:
            self.head = n