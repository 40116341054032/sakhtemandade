class linkedlist:
    def __init__(self):
        self.head = None

    def delfirst(self):
        if (self.head == None):
            return 'empty'
        else:
            self.head = self.head.next
    