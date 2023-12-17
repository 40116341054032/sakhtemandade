class dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class cdlinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("empty")
            return

        current = self.head
        while True:
            print(current.data, end=" --> ")
            current = current.next
            if current == self.head:
                break
        print()