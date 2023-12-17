class clinkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        t = self.head
        if t is None:
            print("empty")
            return
        while (t.next != self.head):
            print(t.data , end="-->")
            t = t.next
        print(t.data)
