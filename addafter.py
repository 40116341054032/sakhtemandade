class node:
    def __init__(self,d):
        self.data = d
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        t = node()
        t = self.head
        while (t != None):
            print(t.data , end="-->")
            t = t.next
        print('None')
        
    def addafter(self,m,d):
        n = node(d)
        t = self.head
        while (t.data != m):
            t = t.next
        n.next = t.next
        t.next = n