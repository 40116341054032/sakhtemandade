def display(self):
    if len(self.stack) <= 0:
        return -1
    else:
        for i in self.stack:
            print(i)