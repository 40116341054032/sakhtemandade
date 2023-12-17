class node:
    def __init__(self,d):
        self.data = d
        self.next = None
        
    def addinstart(self,data):
        n = node(data)
        n.next = self.head
        self.head = n