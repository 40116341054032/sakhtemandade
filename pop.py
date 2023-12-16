def pop(self):
    if len(self.stack) <= 0:
        return -1
    else:
        return self.stack.pop()
