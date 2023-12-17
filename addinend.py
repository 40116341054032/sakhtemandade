class node:
    def __init__(self,d):
        self.data = d
        self.next = None
    
    def addinend(self,data):
        n = node(data)
        t = self.head
        if (t == None):
            self.head = n
        else:
            while (t.next != None):
                t = t.next
            t.next = n