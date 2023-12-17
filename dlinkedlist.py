class dlinkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        t = self.head
        while (t != None):
            print(t.data , end = '<-->')
        print('None')